# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='keywords',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Show title'),
            preserve_default=True,
        ),
    ]
