from django.urls import path
from cache.views import course

urlpatterns = [
    path('course/', course, name="course"),
]
