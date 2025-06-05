from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookie/', include('cookie.urls')),
    path('session/', include('session.urls')),
    path('cache/', include('cache.urls')),
]
