# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_auto_20150318_0902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showcategory',
            options={'verbose_name_plural': 'categor\xedas'},
        ),
        migrations.RemoveField(
            model_name='show',
            name='show_number',
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Mostrar t\xedtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='showcategory',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Mostrar t\xedtulo'),
            preserve_default=True,
        ),
    ]
