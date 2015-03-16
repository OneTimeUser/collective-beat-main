from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
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

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:info')


