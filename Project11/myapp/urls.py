from django.urls import path
from myapp.views import home_view, product_view, AboutView, PostView

urlpatterns = [
    path('home/', home_view, name='home'),
    path('product/<int:pk>/', product_view, name='product'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
]
