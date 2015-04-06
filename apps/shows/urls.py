from django.conf.urls import patterns, url
from apps.shows.views import ShowsList, SearchView

urlpatterns = patterns('',
    url(r'archive/$', ShowsList.as_view(), name='archive'),
    url(r'archive/(?P<category>\w+)/$', ShowsList.as_view(), name='archive_category'),
    url(r'search/$', SearchView.as_view(), name='search'),
    url(r'search/(?P<category>\w+)/$', SearchView.as_view(), name='search_category'),
)