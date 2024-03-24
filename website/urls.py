from django.contrib import admin
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    #This path will correspond to link http://127.0.0.1:8000 and go to views file and look for home function(for function-based program) or class home(for class-based program)
    path('', views.home, name='homepage'),
    path('about', views.about, name = 'aboutpage'),
    path('more', views.more, name = 'morepage')
]
