from django.conf.urls import patterns, url
from apps.accounts.views import AccountInfoView, AccountInfoEdit

urlpatterns = patterns('',
    url(r'^info$', AccountInfoView.as_view(), name='info'),
    url(r'^info/edit$', AccountInfoEdit.as_view(), name='edit_info'),
)