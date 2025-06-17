from django.urls import path
from customer.views import CustomerDashboard, CustomerProfile
app_name = 'customer'

urlpatterns = [
    path('dashboard/', CustomerDashboard.as_view(), name='dashboard'),
    path('profile', CustomerProfile.as_view(), name='profile'),
]
