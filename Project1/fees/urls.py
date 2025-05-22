from django.urls import path
from fees.views import display_btech_fees, display_diploma_fees

urlpatterns = [
    path('btech-fee/', display_btech_fees, name='btechfees'),
    path('diploma-fee/', display_diploma_fees, name='diplomafees'),
]
