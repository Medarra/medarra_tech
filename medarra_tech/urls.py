"""
URL configuration for medarra_tech project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
