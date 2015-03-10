from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView


class AccountInfoView(DetailView):
    template_name = 'accounts/account_info.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(AccountInfoView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user