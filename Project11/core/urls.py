from django.urls import path
from core.views import Home, RedirectToCustomerProfile

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tocustomer/', RedirectToCustomerProfile.as_view(), name='tocustomer'),
]
