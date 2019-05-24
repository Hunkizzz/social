# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include,re_path

from account_social import views

urlpatterns = [
    #url(r'^$',include("account_social.urls")),
    url(r'^login/$',views.user_login, name='login'),
    url(r'^logout/$',views.user_logout, name='logout'),
    re_path(r'^dashboard/$',views.dashboard, name='dashboard'),

]