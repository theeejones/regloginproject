# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from ..reglogin.models import *
from django.contrib import messages

def index(request):
    if "user_id" in request.session:
        data = { "user": User.objects.get(id=request.session['user_id']),
                 "friendlist": User.objects.listfriends(request.session['user_id']),
                 "nonfriendlist": User.objects.listnonfriends(request.session['user_id']) }
        return render(request, 'examapp/index.html', data)
    return redirect('/')

def viewuser(request, friend_id):
    if "user_id" in request.session:
        data = { "user": User.objects.get(id=friend_id) }
        return render(request, 'examapp/viewuser.html', data)
    return redirect('/')

def addfriend(request, friend_id):
    if "user_id" in request.session:
        User.objects.addfriend(request.session['user_id'], friend_id)
        return redirect('/examapp')
    return redirect('/')

def removefriend(request, friend_id):
    if "user_id" in request.session:
        User.objects.removefriend(request.session['user_id'], friend_id)
        return redirect('/examapp')
    return redirect('/')
