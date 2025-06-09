from django.shortcuts import HttpResponse, render
from blog import custom_signals
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    # a = 10/0
    # custom_signals.notification.send(sender=None, request=request, user=["Geeky", "Shows"])
    # return HttpResponse("Hello This is Home page")

    print("i am home view")
    return render(request, 'home.html')


def my_math(request):
    print("I am my_math View")
    a = 10/2
    return render(request, 'math.html', {'a': a})


def user_info(request):
    print("I am user info View")
    context = {'name': 'Rahul'}
    return TemplateResponse(request, 'user.html', context)