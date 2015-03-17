# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150312_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='customemailuser',
            name='gender_other',
            field=models.CharField(max_length=30, null=True, verbose_name='gender (other)', blank=True),
            preserve_default=True,
        ),
    ]
