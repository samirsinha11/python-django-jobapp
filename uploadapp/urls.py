from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("image/", views.upload_image, name='upload_image'),
    path("file/", views.upload_file, name='upload_file'),
]