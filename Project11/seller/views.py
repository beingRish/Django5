from django.shortcuts import HttpResponse
from django.views import View

class SellerDashboard(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Seller Dashboard</h1>")
    
class SellerProfile(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Seller Profile</h1>")