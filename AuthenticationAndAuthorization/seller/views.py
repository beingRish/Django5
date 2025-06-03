from django.shortcuts import render
from core.decorators import login_and_role_required

@login_and_role_required("seller")
def seller_dasboard_view(request):
    return render(request, 'seller/dashboard.html')
