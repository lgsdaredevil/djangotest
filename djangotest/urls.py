# !/usr/bin/python
# -*- coding: utf-8 -*-
"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from study_temp import views as stu

urlpatterns = [
    url(r'^temp_test/$', stu.home, name='temp_test'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'^$', learn_views.html_test, name='home'),
    url(r'^add/(\d+)/(\d+)/$', learn_views.old_add2_redirect),  # 旧地址(导入新地址)
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),  # 新地址
    url(r'^helloworld/$', learn_views.index),  # new
    url(r'^admin/', admin.site.urls),
]
