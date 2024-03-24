from django.contrib import admin
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name = 'aboutpage'),
    path('more', views.more, name = 'morepage')
]
