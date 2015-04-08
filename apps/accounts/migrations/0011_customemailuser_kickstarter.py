# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20150407_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='customemailuser',
            name='kickstarter',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
