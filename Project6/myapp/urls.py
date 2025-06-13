from django.urls import path
from myapp.views import home, product, contact, sync_view, async_view

urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('sync/', sync_view, name='sync_view'),
    path('async/', async_view, name='async_view'),
]
