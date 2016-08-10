# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comicsimage',
            name='comics',
        ),
        migrations.RemoveField(
            model_name='coordinate',
            name='image',
        ),
        migrations.AddField(
            model_name='comics',
            name='pages',
            field=models.ManyToManyField(to='comic.ComicsImage'),
        ),
        migrations.AddField(
            model_name='comicsimage',
            name='coordinates',
            field=models.ManyToManyField(to='comic.Coordinate'),
        ),
    ]
