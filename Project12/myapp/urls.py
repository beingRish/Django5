from django.urls import path
from myapp.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
