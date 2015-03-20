# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_subscriptionbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='customemailuser',
            name='braintree_subscription_id',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriptionbanner',
            name='type',
            field=models.CharField(max_length=1, verbose_name='type', choices=[(b's', 'Sign Up'), (b'u', 'Upgrade')]),
            preserve_default=True,
        ),
    ]
