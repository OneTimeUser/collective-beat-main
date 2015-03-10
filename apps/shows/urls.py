from django.conf.urls import patterns, url
from apps.shows.views import ShowsList, IndexView

urlpatterns = patterns('',
    url(r'$', IndexView.as_view()),
    url(r'archive/$', ShowsList.as_view(), name='archive'),
    url(r'archive/(?P<category>\w+)/$', ShowsList.as_view(), name='archive_category'),
)