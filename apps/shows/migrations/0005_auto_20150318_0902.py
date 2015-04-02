# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_show_url_for_ios'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='showcategory',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
