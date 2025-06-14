from django.urls import path
from myapp.views import AllStudentView, StudentListView, StudentListView1, StudentListView2, StudentListView3

urlpatterns = [
    path('', AllStudentView.as_view(), name='all_student'),
    path('students/', StudentListView.as_view(), name='students'),
    path('students1/', StudentListView1.as_view(), name='students1'),
    path('students2/', StudentListView2.as_view(), name='students2'),
    path('students3/', StudentListView3.as_view(), name='students3'),
]
