# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_friends_+', to='reglogin.User'),
        ),
    ]
