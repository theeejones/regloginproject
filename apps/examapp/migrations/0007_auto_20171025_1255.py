# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0006_auto_20171025_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_friends', to='reglogin.User'),
        ),
    ]
