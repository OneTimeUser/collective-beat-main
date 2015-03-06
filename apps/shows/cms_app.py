from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ShowsApp(CMSApp):
    name = _("Shows App")
    urls = ["apps.shows.urls"]

apphook_pool.register(ShowsApp)