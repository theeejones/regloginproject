# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):

    def login(self, postData):
        email = postData['email'].lower()
        password = postData['password']
        users = self.filter(email = email)
        if len(users):
            user = users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user
        return False

    def userIsValid(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email'].lower()
        password = postData['password']
        cpassword = postData['cpassword']

        errors = []
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(first_name) < 2 or len(first_name) > 255:
            errors.append('First name must be between 2 and 255 characters.')
        if len(last_name) < 2 or len(last_name) > 255:
            errors.append('Last name must be between 2 and 255 characters.')
        if not EMAIL_REGEX.match(email) or len(email) < 6 or len(email) > 255:
            errors.append('The email address you entered is invalid.')
        if not password == cpassword or len(password) < 8 or len(password) > 255:
            errors.append('Your password and password confirmation do not match')

        if not errors:
            users = self.filter(email = email)
            if users:
                errors.append("Email invalid.")
        return errors

    def createUser(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email'].lower()
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = self.create(first_name = first_name, last_name = last_name, email = email, password = password)
        return user.id



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
