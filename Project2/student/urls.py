from django.urls import path
from student.views import all_data, single_data, registration, login, address

urlpatterns = [
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('address/', address, name='address'),
]
