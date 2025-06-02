from django.shortcuts import render

# Create your views here.
def seller_dasboard_view(request):
    return render(request, 'seller/dashboard.html')
