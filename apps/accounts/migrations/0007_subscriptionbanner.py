# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150318_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('type', models.CharField(max_length=1, verbose_name='type', choices=[(b's', 'Reg\xedstrate'), (b'u', 'Upgrade')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
