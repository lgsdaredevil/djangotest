# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-31
    
"""
from django.shortcuts import render


def home(request):
    return render(request, 'home_temp.html')

