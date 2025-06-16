from django.urls import path
from customer.views import CustomerDashboardView, CustomerPasswordChangeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dashboard', login_required(CustomerDashboardView.as_view()), name='customer_dashboard'),
    path('password-change/', CustomerPasswordChangeView.as_view(), name='password_change'),
    
    
    
    # path('profile', permission_requred('product.can_add')(CustomerDashboardView.as_view()), name='profile'),
]
