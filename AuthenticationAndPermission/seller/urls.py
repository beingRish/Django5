from django.urls import path
from seller.views import seller_dasboard_view

urlpatterns = [
    path('dashboard', seller_dasboard_view, name='seller_dashboard'),
    
]
