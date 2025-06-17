from django.urls import path
from seller.views import SellerDashboard, SellerProfile
app_name = 'seller'

urlpatterns = [
    path('dashboard/', SellerDashboard.as_view(), name='dashboard'),
    path('profile', SellerProfile.as_view(), name='profile'),
]
