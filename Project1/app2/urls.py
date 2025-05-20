from django.urls import path
from app2.views import myapp2, myapp2_me

urlpatterns = [
    path('app2/', myapp2, name='myapp2'),
    path('app2_me/', myapp2_me, name='myapp2'),  
]
