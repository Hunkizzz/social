# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include,re_path

from registration import views

urlpatterns = [
    re_path(r'^$', views.RegisterFormView.as_view()),
]