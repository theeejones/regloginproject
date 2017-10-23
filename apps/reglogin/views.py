# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'reglogin/index.html')

def login(request):
    user = User.objects.login(request.POST)
    if user:
        request.session['user_id'] = user.id
        return redirect('/examapp')
    messages.error(request, "Email or password invalid.")
    return redirect('/')

def registration(request):
    errors = User.objects.userIsValid(request.POST)
    if len(errors) == 0:
        request.session['user_id'] = User.objects.createUser(request.POST)
        return redirect('/examapp')
    else:
        for error in errors:
            messages.error(request, error)
    return redirect("/")

def home(request):
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    return render(request, 'reglogin/home.html', { 'user': user })

def logout(request):
    request.session.clear()
    return redirect('/')
