# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-26 03:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='County',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
