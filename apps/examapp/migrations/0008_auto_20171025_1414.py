# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0007_auto_20171025_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='friend_owner',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
