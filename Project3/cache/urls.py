from django.urls import path
from cache.views import home, course, result
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', home, name="home"),
    path('home', cache_page(60)(home), name="home"),
    path('index', cache_page(90)(home), name="home"),
    path('course/', course, name="course"),
    path('result/', cache_page(30)(result), name="result"),
]
