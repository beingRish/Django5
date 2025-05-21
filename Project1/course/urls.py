from django.urls import path
from course.views import learn_django, learn_fastapi, learn_python

urlpatterns = [
    path('dj/', learn_django, name='learn_django'),
    path('fst/', learn_fastapi, name='learn_fastapi'),
    path('py/', learn_python, name='learn_python'),

]
