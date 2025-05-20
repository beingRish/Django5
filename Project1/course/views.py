from django.shortcuts import render

# Create your views here.

def learn_django(req):
    coursename = {'cname': 'Django 5.1'}
    return render(req, 'course/django.html', coursename)

def learn_fastapi(req):
    seats = 10
    coursedetails = {
        'cname': 'FAST API',
        'version': '3.1',
        'st':seats
    }

    return render(req, 'course/fastapi.html', coursedetails)