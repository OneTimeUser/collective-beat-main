# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customemailuser',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2015, 3, 6, 12, 49, 26, 336784, tzinfo=utc), verbose_name=b'Date of Birth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='is_getting_the_news',
            field=models.BooleanField(default=True, verbose_name=b'Subscribed to news and updates'),
            preserve_default=True,
        ),
    ]
