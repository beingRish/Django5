from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html')
    
class RedirectToCustomerProfile(View):
    def get(self, request, *args, **kwargs):
        return redirect('customer:profile')
    
# class RedirectToCustomerProfile(View):
#     def get(self, request, *args, **kwargs):
#         success_url = reverse_lazy('customer:profile')
#         return redirect(success_url)
