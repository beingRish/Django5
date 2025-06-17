from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('seller/', include('seller.urls')),
    path('customer/', include('customer.urls')),
    # path('customer/', include('customer.urls', namespace='v1')),
    # path('customer/', include('customer.urls', namespace='v2')),
]
