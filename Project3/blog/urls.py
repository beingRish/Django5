from django.urls import path
from blog.views import home, my_math, user_info

urlpatterns = [
    path('', home, name='home'),
    path('math', my_math, name='math'),
    path('user', user_info, name='user'),
]
