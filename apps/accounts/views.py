from allauth.account.utils import send_email_confirmation, get_next_redirect_url
from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from djpj import pjax_block
from apps.accounts.forms import AccountEditForm, EmailSubscriptionForm


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


class SubscriptionsEditView(UpdateView):
    http_method_names = ['post']
    form_class = EmailSubscriptionForm

    def get_object(self, queryset=None):
        return get_user_model().objects.get(pk=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, _('Email subscriptions settings changed'))
        return super(SubscriptionsEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:info')


class SubscriptionSignupView(SignupView):
    def get_success_url(self):
        # @TODO this url is for testing only!!!
        to_plan_redirect_url = reverse('accounts:info')
        # Explicitly passed ?next= URL takes precedence
        ret = (get_next_redirect_url(self.request,
                                     self.redirect_field_name)
               or to_plan_redirect_url)
        return ret
