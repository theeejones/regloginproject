# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..reglogin.models import User
import datetime

class Character(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="user_characters")

class Item(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ManyToManyField(Character, "owned_items")