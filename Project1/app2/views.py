from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myapp2(request):
    return HttpResponse("<h1>My App 2 Page</h1>")

def myapp2_me(request):
    return HttpResponse("My App 2 Me Page")