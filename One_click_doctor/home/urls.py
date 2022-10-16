from ast import For
from django.contrib import admin
from django.urls import path, include
from home import views



urlpatterns = [
    path("", views.index, name='home'),
    path("Aurveda", views.Aurdeva, name='Aurveda'),
    path("Acupressure", views.Acupressure, name='Acupressure'),
    path("Article", views.Article, name='Article'),
    path("top_reasons", views.top_reasons, name='reasons'),
    path("Helpful_Herbs", views.Helpful_Herbs,name='Helpful_Herbs' ),
    path('accounts/', include('django.contrib.auth.urls')),
]
'''path('One-click_doctor/<int:tweets_id>', tweet_detail_view),
                path('One-click_doctor', tweet_list_view)'''
#path("About_us", views.About_us, name='About_us'),


