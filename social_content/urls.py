"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

from social_content import views

app_name = 'social_content'

urlpatterns = [
    url(r'^create/$', views.content_create, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail, name='detail'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', views.content_edit, name='edit'),
    re_path(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/delete/$', views.delete_content, name='delete'),
    path('like/',views.content_like,name='like'),
    url(r'^add_to_favorites/$',views.AddArticlesToFavorites, name='add_to_favorites'),

]
