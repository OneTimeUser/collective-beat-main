from django.conf.urls import patterns, url
from apps.accounts.views import AccountInfoView

urlpatterns = patterns('',
    url(r'^info$', AccountInfoView.as_view(), name='info'),
)