"""LibraryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from library import views
app_name = 'library'
urlpatterns = [
    path('',views.homeview,name = 'homeview'),
    url(r'^login/$',views.user_login, name = 'login'),
    url(r'^signout/$',views.signout, name='signout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile=(?P<profile>[\w]+)$', views.user_profile, name = 'user_profile'),
    url(r'^book=(?P<book_id>[\w]+)$',views.book_detail,name = 'book_detail'),
]
