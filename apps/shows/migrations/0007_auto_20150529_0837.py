# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_auto_20150402_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.ManyToManyField(related_name='shows', to='shows.ShowCategory'),
            preserve_default=True,
        ),
    ]
