# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150310_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='customemailuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customemailuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='gender', choices=[(b'm', 'Male'), (b'f', 'Female'), (b'o', 'Other')]),
            preserve_default=True,
        ),
    ]
