# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *

def index(request):
    if "user_id" in request.session:
        c = Character.objects.get(id=1)
        return render(request, 'examapp/index.html')
    return redirect('/')