# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customemailuser_gender_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='nombre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='apellidos', blank=True),
            preserve_default=True,
        ),
    ]
