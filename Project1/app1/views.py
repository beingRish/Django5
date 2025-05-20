from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1>Learn Python</h1>')

def learn_math(request):
    a = 10 + 20
    return HttpResponse(a)

def learn_php(request):
    lang = '<h1>Hello PHP</h1>'
    return HttpResponse(lang)