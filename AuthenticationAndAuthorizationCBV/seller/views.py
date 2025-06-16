from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.misins import IsSellerMixin

class SellerDashboardView(LoginRequiredMixin,IsSellerMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'seller/dashboard.html')