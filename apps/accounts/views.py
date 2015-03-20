from braintree import SuccessfulResult
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView
from djpj import pjax_block
from allauth.account.utils import send_email_confirmation, get_next_redirect_url
from allauth.account.views import SignupView
from apps.accounts.models import SubscriptionPlans
from apps.accounts.forms import AccountEditForm, EmailSubscriptionForm, ChangeSubscriptionPlanForm


class AccountInfoView(DetailView):
    template_name = 'accounts/account_info.html'

    @method_decorator(login_required())
    @method_decorator(pjax_block('pjax-content', title_block='head_title'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountInfoView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AccountInfoView, self).get_context_data(**kwargs)
        context['subscriptions_form'] = EmailSubscriptionForm(instance=self.request.user)

        return context


class AccountInfoEdit(UpdateView):
    form_class = AccountEditForm
    template_name = 'accounts/account_info_edit.html'

    @method_decorator(login_required())
    @method_decorator(pjax_block('pjax-content', title_block='head_title'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountInfoEdit, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        super(AccountInfoEdit, self).form_valid(form)

        if form.cleaned_data['email'] != self.request.user.email:
            send_email_confirmation(self.request, self.object)

        messages.success(self.request, _('Profile details updated.'))
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return get_user_model().objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse('accounts:info')


class SubscriptionsEditView(FormView):
    template_name = 'accounts/plan_change.html'
    form_class = ChangeSubscriptionPlanForm
    plan_data = None

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        self.plan_data = SubscriptionPlans.plan_by_braintree_id(kwargs['plan_id'])

        # preventing manual link navigation
        if request.user.subscription_plan == self.plan_data['id']:
            return HttpResponseRedirect(reverse('accounts:info'))

        return super(SubscriptionsEditView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # cancelling previous user's subscription (if any):
        if self.request.user.is_paid_member and self.request.user.braintree_subscription_id:
            result = self.request.user.cancel_current_subscription()
            if type(result) is not SuccessfulResult:
                messages.error(self.request, result.message)

        if self.plan_data['id'] != SubscriptionPlans.FREE:
            # creating new subscription
            result = self.request.user.create_subscription(
                payment_method_nonce=form.cleaned_data["payment_method_nonce"],
                plan_braintree_id=self.plan_data['braintree_id']
            )

            if result.is_success:
                result_message = _("Subscription Status: {0}").format(result.subscription.status)
            else:
                result_message = _("Error: {0}").format(result.message)
        else:
            result_message = _('Subscription cancelled')

        # messages.success(self.request, _('Subscriptions plan settings changed'))
        messages.success(self.request, result_message)

        return super(SubscriptionsEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SubscriptionsEditView, self).get_context_data(**kwargs)
        context['braintree_client_token'] = self.request.user.braintree_client_token
        context['plan_to_change'] = self.plan_data
        context['change_to_free'] = self.plan_data['id'] == SubscriptionPlans.FREE

        return context

    def get_success_url(self):
        return reverse('accounts:info')


class SubscriptionSignupView(SignupView):
    def get_success_url(self):
        to_plan_redirect_url = reverse('accounts:change_plan', kwargs={
            'plan_id': SubscriptionPlans.available_plans_by_ids()[self.request.POST['subscription_plan']][
                'braintree_id']})
        ret = (get_next_redirect_url(self.request,
                                     self.redirect_field_name)
               or to_plan_redirect_url)
        return ret
