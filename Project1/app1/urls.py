from django.urls import path
from app1.views import home, myapp1, learn_django

urlpatterns = [
    path('', home, name='home'),
    path('app1/', myapp1, name='myapp1'), 
    path('py/', learn_django),
    path('dj/', learn_django, {'status': 'OK'}),   
]
