from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'account/home.html')

def login_view(request):
    if request.method == "POST":
        return redirect('customer_dashboard')
    return render(request, 'account/login.html')

def register_view(request):
    return render(request, 'account/register.html')

def password_reset_view(request):
    return render(request, 'account/password_reset.html')

def password_reset_confirm_view(request):
    return render(request, 'account/password_reset_confirm.html')
