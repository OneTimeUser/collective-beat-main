# from fabric.api import run
import os
import urllib

from fabric.contrib import django
from fabric.operations import local
from fabric.utils import puts

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
django.settings_module('collective_beat.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.files import File
from django.utils import timezone

from apps.shows.models import ShowCategory, Show


def add_admin():
    user_model = get_user_model()
    admin = user_model(email='admin@example.com')
    admin.is_superuser = True
    admin.is_staff = True
    admin.set_password('admin')
    admin.save()


def add_flatpages():
    current_site = Site.objects.get_current()
    try:
        FlatPage.objects.get(sites__in=[current_site], url='/contact/')
    except FlatPage.DoesNotExist:
        contacts_page = FlatPage.objects.create(url='/contact/', title='CONTACTO',
                                                content='<p>Some text on the contacts page</p>')
        contacts_page.sites = [current_site]


def add_show_categories():
    show_categories = [
        {'title': 'politics'},
        {'title': 'culture'},
        {'title': 'business'},
    ]
    for sc in show_categories:
            ShowCategory.objects.create(**sc)


def add_shows():
    images_dir = os.path.join(BASE_DIR, 'collective_beat/static/img/')
    stream_url = 'rtmp://flash.oit.duke.edu/vod/_definst_'
    shows = [
        {
            'title': 'First show',
            'date': timezone.now(),
            'description': 'this is the description for the first podcast show',
            'url': stream_url,
            'url_for_ios': stream_url,
        },
        {
            'title': 'Second show',
            'date': timezone.now(),
            'description': 'this is the description for the second podcast show',
            'url': stream_url,
            'url_for_ios': stream_url,
        },
        {
            'title': 'Third show',
            'date': timezone.now(),
            'description': 'this is the description for the third podcast show',
            'url': stream_url,
            'url_for_ios': stream_url,
        },
        {
            'title': 'Fourth show',
            'date': timezone.now(),
            'description': 'this is the description for the fourth podcast show',
            'url': stream_url,
            'url_for_ios': stream_url,
        }
    ]

    img_filename = 'podcast-img6.jpg'
    result_img = urllib.urlretrieve(os.path.join(images_dir, img_filename))
    img_file = File(open(result_img[0]))
    for s in shows:
        show = Show.objects.create(**s)
        show.category.add(ShowCategory.objects.get(pk=1))
        show.image.save(img_filename, img_file, True)


def add_editors():
    editors, created = Group.objects.get_or_create(name='Editors')
    if created:
        add_flatpage = Permission.objects.get(codename='add_flatpage')
        change_flatpage = Permission.objects.get(codename='change_flatpage')
        delete_flatpage = Permission.objects.get(codename='delete_flatpage')

        add_showcategory = Permission.objects.get(codename='add_showcategory')
        change_showcategory = Permission.objects.get(codename='change_showcategory')
        delete_showcategory = Permission.objects.get(codename='delete_showcategory')

        add_show = Permission.objects.get(codename='add_show')
        change_show = Permission.objects.get(codename='change_show')
        delete_show = Permission.objects.get(codename='delete_show')

        editors.permissions.add(add_flatpage, change_flatpage, delete_flatpage,
                                add_showcategory, change_showcategory, delete_showcategory,
                                add_show, change_show, delete_show)
        editors.save()


def initial_data():
    puts('==> Hi there! :)')
    puts('==> Installing the requirements...')
    local('pip install -r requirements/dev.txt ')
    puts('==> Creating the db...')
    local('python manage.py migrate')
    local('bower install')
    puts('==> Creating the superuser...')
    add_admin()
    puts('==> Adding initial data...')
    add_flatpages()
    add_show_categories()
    add_shows()
    add_editors()
    puts('==> All done. Please do your thing and leave :)')
