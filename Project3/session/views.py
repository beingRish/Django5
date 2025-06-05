from django.shortcuts import render
from datetime import  datetime, timedelta, timezone


def setsession(request):
    request.session['fname'] = 'Rishabh'
    request.session['lname'] = 'Singh'
    # request.session.set_expiry(10)  # Value in seconds
    # request.session.set_expiry(0)   # session expire in browser close
    return render(request, 'session/setsession.html')


def getsession(request):
    # first_name = request.session['fname']
    first_name = request.session.get('fname')
    last_name = request.session.get('lname')
    # first_name = request.session.get('fname', 'Guest')
    return render(request, 'session/getsession.html', {'first_name': first_name, 'last_name': last_name})


def delsession(request):
    if 'lname' in request.session:
        del request.session['lname']
    return render(request, 'session/delsession.html')


def flushsession(request):
    request.session.flush()
    return render(request, 'session/flushsession.html')


def sessionmethodsinview(request):
    keys = request.session.keys()
    print(keys)
    items = request.session.items()
    print(items)
    age = request.session.setdefault('age', 31)
    print('age:', age)

    
    session_cookies_age = request.session.get_session_cookie_age()
    print('session cookies age:', session_cookies_age)

    
    expire_age = request.session.get_expiry_age()
    print('Expire age:', expire_age)

    
    expire_date = request.session.get_expiry_date()
    print('Expire date:', expire_date)

    
    get_expire_at_browser_close = request.session.get_expire_at_browser_close()
    print('Expire at browser close:', get_expire_at_browser_close)

    return render(request, 'session/sessionmethodsinview.html')


def sessionmethodsintemplate(request):
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'session/sessionmethodsintemplate.html', {'keys': keys, 'items': items})


def sessionclear(request):
    request.session.clear_expired()
    return render(request, 'session/sessionclear.html')


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'session/settestcookie.html')


def checktestcookie(request):
    request.session.test_cookie_worked()
    return render(request, 'session/checktestcookie.html')


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'session/deltestcookie.html')
