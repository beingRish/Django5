from django.shortcuts import HttpResponse
from django.views import View

class CustomerDashboard(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Customer Dashboard</h1>")
    
class CustomerProfile(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Customer Profile</h1>")