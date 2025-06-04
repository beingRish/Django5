from django.urls import path
from student.views import setcookie, getcookie, delcookie, setsignedcookie, getsignedcookie

urlpatterns = [
    path('set/', setcookie),
    path('get/', getcookie),
    path('del/', delcookie),
    path('setsigned/', setsignedcookie),
    path('getsigned/', getsignedcookie),
]
