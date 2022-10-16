"""One_click_doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from home.views import (post_list_view, tweet_detail_view
, tweet_create_view)
admin.site.site_header  =  "One Click Doctor Admin"  
admin.site.site_title  =  "One Click Doctor ADMIN Portal"
admin.site.index_title  =  "Welcome to One Click Doctor Reserches Portal"

urlpatterns = [ 
    path('admin/',admin.site.urls),
    path('',include('home.urls')),
    path('create-tweet', tweet_create_view),
    path('home/<int:tweet_id>', tweet_detail_view),
    path('home', post_list_view),
    
] 
'''path('accounts/', include('django.contrib.auth.urls')),'''