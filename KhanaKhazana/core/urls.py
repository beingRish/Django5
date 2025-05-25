from django.urls import path
from core.views import home, menu, tracking, reservation, contact

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('tracking/', tracking, name='track'),
    path('reservation/', reservation, name='reservation'),
    path('contact/', contact, name='contact'),
]
