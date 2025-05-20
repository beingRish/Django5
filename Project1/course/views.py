from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def php_course(req):
    return HttpResponse(f'<h1>Learn PHP Step by Step</h1>')