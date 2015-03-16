from allauth.account.utils import send_email_confirmation
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
from apps.accounts.forms import AccountEditForm


class AccountInfoView(DetailView):
    template_name = 'accounts/account_info.html'

    @method_decorator(login_required())
    @method_decorator(pjax_block('content'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountInfoView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user


class AccountInfoEdit(UpdateView):
    form_class = AccountEditForm
    template_name = 'accounts/account_info_edit.html'

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


