from django.shortcuts import render
from django.views import View

class SellerDashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'seller/dashboard.html')