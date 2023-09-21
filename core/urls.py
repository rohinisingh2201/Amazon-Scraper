from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('new.html/', views.results, name = 'new'),
]