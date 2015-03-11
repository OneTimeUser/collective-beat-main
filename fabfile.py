# from fabric.api import run
from fabric.contrib import django
django.settings_module('collective_beat.settings')

import django
django.setup()

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
# from django.conf import settings


def initial_data():
    current_site = Site.objects.get_current()
    try:
        FlatPage.objects.get(sites__in=[current_site], url='/contact/')
    except FlatPage.DoesNotExist:
        contacts_page = FlatPage.objects.create(url='/contact/', title='CONTACTO',
                                                content='<p>Some text on the contacts page</p>')
        contacts_page.sites = [current_site]
