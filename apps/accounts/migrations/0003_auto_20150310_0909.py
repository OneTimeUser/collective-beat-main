# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150306_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customemailuser',
            name='birthdate',
            field=models.DateField(null=True, verbose_name=b'Date of Birth'),
            preserve_default=True,
        ),
    ]
