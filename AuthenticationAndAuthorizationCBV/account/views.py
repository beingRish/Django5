from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/home.html')
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/login.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, 'customer/dashboard.html')
    
    
class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/register.html')  
    
class CustomPasswordResetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/password_reset.html')
    
class PasswordResetConfirmView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/password_reset_confirm.html')
