from __future__ import print_function
from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from apps.shows.views import IndexView
from apps.accounts.views import SubscriptionSignupView

admin.autodiscover()

# urlpatterns = i18n_patterns('',
urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    (r'^account/', include('apps.accounts.urls', namespace='accounts')),
    (r'^shows/', include('apps.shows.urls', namespace='shows')),
    (r'^pages', include('django.contrib.flatpages.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

# fixme - need to get site settings dynamically (lazily querying the database)
# if not Site.objects.get_current().free_version:
urlpatterns += patterns('',
    url(r"^accounts/signup/$", SubscriptionSignupView.as_view(), name="account_signup"),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),
)

urlpatterns += i18n_patterns('',
    (r'^admin/', include(admin.site.urls)),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns
