# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='url_for_ios',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
