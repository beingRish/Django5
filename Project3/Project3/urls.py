from django.contrib import admin
from django.urls import path, include
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookie/', include('cookie.urls')),
    path('session/', include('session.urls')),
    path('cache/', include('cache.urls')),
    path('home/', home),
]
