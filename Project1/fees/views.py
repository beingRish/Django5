from django.shortcuts import render

# Create your views here.

def display_btech_fees(req):
    return render(req, 'fees/btech.html', {'fee':50})

def display_diploma_fees(req):
    context = {'data': 'Hello I am django developer. I am also creating educational videos. I am not human.'}
    return render(req, 'fees/diploma.html', context)
