from django.urls import path
from myapp.views import home, product, contact

urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
]
