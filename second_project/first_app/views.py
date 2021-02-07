from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import json


# Create your views here.
def home(request):
    context = {"name": "Eric",
               "surname": "Sargsyan"
    }
    return render(request, 'first_app/home.html', context)
    # return HttpResponse("<h1>This is home page</h1>")




def actors(request):
    with open('data.json', 'r') as movies:
        # persons = {}
        data = json.load(movies)
        # for i in data['items']:
            # persons.append(i)
    return render(request, "first_app/actors.html", data)
