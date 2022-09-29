from multiprocessing import context
#from tkinter import EXCEPTION
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.template import loader

from app.models import JobPost


job_title = ['First job',
             'Second Job',
             'Third Job'
]

job_description=['First Job description',
                 'Second Job description',
                 'Third Job description'
]

list1 ={'alpha', 'beta', 'gama'} 

# Create your views here.
def hello(request):
    is_autheticated = False
    age = 22
    context={"name":"Django", 'age':22, "is_autheticated":is_autheticated, "list":list1}
    return render(request, "app/hello.html", context )
def jobdetails(request, job_id):
    try:
        #retHtml = f'<h1> {job_title[job_id]}</h1> <h3>{job_description[job_id]}</h3>'   
        #context = {'retHtml':retHtml}
        jobs = JobPost.objects.get(id=job_id)
        context = {'job':jobs}
        return render(request, "app/jobDetails.html", context )
    except:
        return HttpResponseNotFound('Not found')

def job_details(request):
    jobs = JobPost.objects.all()
    context = {'jobs':jobs}
    return render(request, "app/index.html", context)
def jobs(request):
    return redirect('/')
