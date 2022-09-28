
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.job_details, name='job_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:job_id>', views.jobdetails, name='job_detail'),
    path('jobs/', views.jobs, name='jobs')
]