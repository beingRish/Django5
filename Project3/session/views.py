from django.shortcuts import render
from datetime import  datetime, timedelta, timezone


def setsession(request):
    return render(request, 'session/setsession.html')


def getsession(request):
    return render(request, 'session/getsession.html')


def delsession(request):
    return render(request, 'session/delsession.html')


def flushsession(request):
    return render(request, 'session/flushsession.html')


def sessionmethodsinview(request):
    return render(request, 'session/sessionmethodsinview.html')


def sessionmethodsintemplate(request):
    return render(request, 'session/sessionmethodsintemplate.html')

def sessionclear(request):
    return render(request, 'session/sessionclear.html')


def settestcookie(request):
    return render(request, 'session/settestcookie.html')


def checktestcookie(request):
    return render(request, 'session/checktestcookie.html')


def deltestcookie(request):
    return render(request, 'session/deltestcookie.html')
