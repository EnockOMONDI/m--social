# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 23:41
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
    ]
