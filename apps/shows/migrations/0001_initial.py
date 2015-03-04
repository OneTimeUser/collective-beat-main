# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('keywords', models.CharField(max_length=255, verbose_name='Show title')),
                ('image', models.ImageField(upload_to=b'')),
                ('url', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('show_number', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShowCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Show title')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='show',
            name='category',
            field=models.ManyToManyField(to='shows.ShowCategory'),
            preserve_default=True,
        ),
    ]
