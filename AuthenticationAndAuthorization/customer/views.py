from django.shortcuts import render

# Create your views here.
def customer_dasboard_view(request):
    return render(request, 'customer/dashboard.html')

def password_change_view(request):
    return render(request, 'customer/password_change.html')