from django.shortcuts import render
from django.views import View

class CustomerDashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/dashboard.html')
    
class CustomerPasswordChangeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/password_change.html')