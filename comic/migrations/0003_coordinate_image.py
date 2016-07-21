# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0002_coordinate'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinate',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comic.ComicsImage'),
        ),
    ]