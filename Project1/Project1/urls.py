# from django.contrib import admin
# from django.urls import path
# from app1 import views as ap1
# from app2 import views as ap2

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', ap1.home, name='home'),
#     path('app1/', ap1.myapp1, name='myapp1'),
#     path('app2/', ap2.myapp2, name='myapp2'),
#     path('app2/', ap2.myapp2_me, name='myapp2'),

# ]

from django.contrib import admin
from django.urls import path
from app1.views import home, myapp1
from app2.views import myapp2, myapp2_me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('app1/', myapp1, name='myapp1'),
    path('app2/', myapp2, name='myapp2'),
    path('app2_me/', myapp2_me, name='myapp2'),

]
