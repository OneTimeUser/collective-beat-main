# from fabric.api import run
import datetime
import os
import urllib
from fabric.contrib import django
from fabric.operations import local
from fabric.utils import puts

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
django.settings_module('collective_beat.settings')

import django
django.setup()

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.files import File

from apps.shows.models import ShowCategory, Show


def initial_data():
    puts('==> Hi there! :)')
    puts('==> Installing the requirements...')
    local('pip install -r requirements/dev.txt ')
    puts('==> Creating the db...')
    local('python manage.py migrate')
    puts('==> Creating the superuser...')
    local('python manage.py createsuperuser')
    puts('==> Adding initial data...')

    current_site = Site.objects.get_current()
    try:
        FlatPage.objects.get(sites__in=[current_site], url='/contact/')
    except FlatPage.DoesNotExist:
        contacts_page = FlatPage.objects.create(url='/contact/', title='CONTACTO',
                                                content='<p>Some text on the contacts page</p>')
        contacts_page.sites = [current_site]

    images_dir = os.path.join(BASE_DIR, 'collective_beat/cb_static/img/')
    stream_url = 'rtmp://flash.oit.duke.edu/vod/_definst_'

    show_categories = [
        {'title': 'politics'},
        {'title': 'culture'},
        {'title': 'business'},
    ]

    for sc in show_categories:
            ShowCategory.objects.create(**sc)

    shows = [
        {
            'title': 'First show',
            'date': datetime.date,
            'show_number': '00001',
            'description': 'this is the description for the first podcast show',
            'url': stream_url,
            'image': File(urllib.urlretrieve(os.path.join(images_dir, 'podcast-img3.jpg'))),
        },
        {
            'title': 'Second show',
            'date': datetime.date,
            'show_number': '00002',
            'description': 'this is the description for the second podcast show',
            'url': stream_url,
            'image': File(urllib.urlretrieve(os.path.join(images_dir, 'podcast-img4.jpg'))),
        },
        {
            'title': 'Third show',
            'date': datetime.date,
            'show_number': '00003',
            'description': 'this is the description for the third podcast show',
            'url': stream_url,
            'image': File(urllib.urlretrieve(os.path.join(images_dir, 'podcast-img5.jpg'))),
        },
        {
            'title': 'Fourth show',
            'date': datetime.date,
            'show_number': '00004',
            'description': 'this is the description for the fourth podcast show',
            'url': stream_url,
            'image': File(urllib.urlretrieve(os.path.join(images_dir, 'podcast-img6.jpg'))),
        }
    ]

    for s in shows:
        show = Show.objects.create(**s)
        show.category.add(ShowCategory.objects.get(pk=1))


    puts('==> All done. Please do your thing and leave :)')