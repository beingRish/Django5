from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.misins import IsSellerMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class SellerDashboardView(IsSellerMixin, View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, 'seller/dashboard.html')


# class SellerDashboardView(View):
    
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'seller/dashboard.html')


# @method_decorator(login_required, name='dispatch')
# class SellerDashboardView(View):    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'seller/dashboard.html')


# @method_decorator(permission_required('product.can_add'), name='dispatch')
# class SellerDashboardView(View):    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'seller/dashboard.html')


# @method_decorator([login_required, permission_required('product.can_add')], name='dispatch')
# class SellerDashboardView(View):    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'seller/dashboard.html')