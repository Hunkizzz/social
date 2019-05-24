# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin, auth
from django.urls import path,include,re_path
from django.views.generic import ListView

from account_social import views
from social_content.models import Content
from account_social.models import Profile

urlpatterns = [
    #url(r'^$',include("account_social.urls")),
    url(r'^login/$',views.user_login, name='login'),
    url(r'^logout/$',views.user_logout, name='logout'),
    url(r'^news/$', ListView.as_view(queryset=Content.objects.all().order_by("-user")[:20],
                                      template_name="account/news.html")),
    re_path(r'^dashboard/$',views.dashboard, name='dashboard'),
    re_path(r'^edit/$', views.edit_profile, name='edit')

]