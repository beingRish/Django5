from django.urls import path
from course.views import learn_django, learn_fastapi, learn_python

urlpatterns = [
    path('dj/', learn_django, name='django'),
    path('fst/', learn_fastapi, name='fastapi'),
    path('py/', learn_python, name='python'),

]
