# !/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponse(u"Hello World!")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def html_test(request):
    return render(request, 'home.html')


def old_add2_redirect(request, a, b):
    """
    旧地址跳转
    :param request:
    :param a:
    :param b:
    :return:
    """
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )