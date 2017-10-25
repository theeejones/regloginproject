# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
import datetime

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
        birthday = postData['birthday']
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
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d')
        except ValueError:
            errors.append("Incorrect data format, should be YYYY-MM-DD")
        if not password == cpassword:
            errors.append('Your password and password confirmation do not match.')
        if len(password) < 8 or len(password) > 255:
            errors.append('Your password must be between 8 and 255 characters.')

        if not errors:
            users = self.filter(email = email)
            if users:
                errors.append("Email invalid.")
        return errors

    def createUser(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email'].lower()
        birthday = postData['birthday']
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = self.create(first_name = first_name, last_name = last_name, email = email, birthday = birthday, password = password)
        return user.id

    def listfriends(self, user_id):
        return self.get(id=user_id).friends.all()

    def listnonfriends(self, user_id):
        return self.exclude(friends=self.get(id=user_id))

    def addfriend(self, user_id, friend_id):
        self.get(id=user_id).friends.add(self.get(id=friend_id))

    def removefriend(self, user_id, friend_id):
        self.get(id=user_id).friends.remove(self.get(id=friend_id))



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    friends = models.ManyToManyField('self')
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
