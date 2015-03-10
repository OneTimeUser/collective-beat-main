# from fabric.api import run
from fabric.contrib import django
django.settings_module('collective_beat.settings')

import django
django.setup()

from cms.api import create_page
# from django.conf import settings


def init_cms_page_structure():
    home = create_page(title='Home', template='page.html', language='en',
                       published=True,
                       apphook='ShowsApp', apphook_namespace='shows')
    create_page(parent=home, template='page.html', language='en',
                title='Archive', slug='archive',
                published=True, in_navigation=True)

    static_root = create_page(title='Static pages root', template='page.html', language='en',
                              redirect='/', reverse_id='footer_root',
                              published=True)
    create_page(parent=static_root, title='Contact information', template='page.html', language='en',
                slug='contacts', menu_title='Contacts', meta_description='some contacts data description',
                published=True, in_navigation=True)
