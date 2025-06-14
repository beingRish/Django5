from django.urls import path
from myapp.views import AllStudentView

urlpatterns = [
    path('', AllStudentView.as_view(), name='all_student'),
]
