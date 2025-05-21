from django.shortcuts import render

# Create your views here.

def display_btech_fees(req):
    return render(req, 'fees/btech.html', {'fee':50})

def display_diploma_fees(req):
    return render(req, 'fees/diploma.html', {'fee':100})
