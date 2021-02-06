from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    return HttpResponse("This is home page")


def greeting(request):
    return HttpResponse("Hi this is my first project on django framework")


def intro(request):
    return HttpResponse("This is introduction page")


def date(request):
    return HttpResponse(f"Current date: {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")


def task(request):
    a = {}
    for i in range(1,16):
        a.update({i: i ** 2})
    return HttpResponse(str(a))
