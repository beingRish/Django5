from django.urls import path
from student.views import all_data, single_data, registration, login, address, demo_form, reg_success

urlpatterns = [
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('address/', address, name='address'),
    path('demo-form/', demo_form, name='demo_form'),
    path('success/', reg_success, name='reg_success'),
]
