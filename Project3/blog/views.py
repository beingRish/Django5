from django.shortcuts import HttpResponse
from blog import custom_signals

# Create your views here.
def home(request):
    # a = 10/0
    custom_signals.notification.send(sender=None, request=request, user=["Geeky", "Shows"])
    return HttpResponse("Hello This is Home page")