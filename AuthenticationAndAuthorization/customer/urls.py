from django.urls import path
from customer.views import customer_dasboard_view, password_change_view

urlpatterns = [
    path('dashboard', customer_dasboard_view, name='customer_dashboard'),
    path('password-change/', password_change_view, name='password_change'),
    
]
