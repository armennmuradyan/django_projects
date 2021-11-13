from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    return HttpResponse("Hello from Django app")


def greeting(request):
    return HttpResponse("Hi everyone")


def introduction(request):
    return HttpResponse("second project")


def date_time(request):
    return HttpResponse(datetime.now())


def task(request):
    dict_ = {}
    for i in range(16):
        dict_[i] = i**2
    print(dict_)
    return HttpResponse(dict_)