# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150319_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_key', models.CharField(max_length=40)),
                ('ip_address', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Fecha de Nacimiento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Pa\xeds'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nombre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='Sexo', choices=[(b'm', 'Masculino'), (b'f', 'Femenino'), (b'o', 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='gender_other',
            field=models.CharField(max_length=30, null=True, verbose_name='Sexo (otro)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='is_getting_the_news',
            field=models.BooleanField(default=True, verbose_name='Suscrito a noticias de \xfaltima hora'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Apellido', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customemailuser',
            name='subscription_plan',
            field=models.CharField(max_length=1, choices=[(b'f', 'Gratis'), (b'm', 'Mensual'), (b'a', 'Anual')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriptionbanner',
            name='type',
            field=models.CharField(max_length=1, verbose_name='type', choices=[(b's', 'Inscr\xedbete'), (b'u', 'Ascender')]),
            preserve_default=True,
        ),
    ]
