from django.shortcuts import render
from datetime import datetime

# Create your views here.

# def learn_django(req):
#     coursename = {'cname': 'Django 5.1'}
#     return render(req, 'course/django.html', coursename)

def learn_fastapi(req):
    seats = 10
    stu = {
        'stu1': {
            'name': 'Rishabh',
            'roll': 101
        },
        'stu2': {
            'name': 'Ritik',
            'roll': 102
        },
        'stu3': {
            'name': 'Shashank',
            'roll': 103
        },
        'stu4': {
            'name': 'Vishwjeet',
            'roll': 104
        },
    }
    coursedetails = {
        'cname': 'FAST API',
        'version': '3.1',
        'st':seats,
        'student':stu
    }

    return render(req, 'course/fastapi.html', coursedetails)

def learn_django(req):
    coursedetails = {
        'cname': 'Django',
        'desc':'Django is awesome web framework',
        'dt': datetime.now(),
        'course_price': {
            'p1': 56.24321,
            'p2': 56.000,
            'p3': 56.37000
        },
        'course_started': True,
        'seat_available': 5,
        'studenst_names': ["Rishabh", "Ristik", "Shashank", "Vishwjeet"]
    }

    return render(req, 'course/django.html', coursedetails)