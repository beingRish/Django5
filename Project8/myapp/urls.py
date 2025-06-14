from django.urls import path
from myapp.views import AllStudentView, SingleStudentView, StudentListView, StudentListView1, StudentListView2, StudentListView3, StudentDetailView, StudentDetailView1, StudentDetailView2, StudentDetailView3

urlpatterns = [
    path('', AllStudentView.as_view(), name='all_student'),
    path('<int:pk>/', SingleStudentView.as_view(), name='single_student'),

    # URLs for ListView
    path('students/', StudentListView.as_view(), name='students'),
    path('students1/', StudentListView1.as_view(), name='students1'),
    path('students2/', StudentListView2.as_view(), name='students2'),
    path('students3/', StudentListView3.as_view(), name='students3'),

    # URLs for DetailView
    path('student/<int:pk>/', StudentDetailView.as_view(), name='studentdetail'),
    path('student1/<int:my_id>/', StudentDetailView1.as_view(), name='studentdetail1'),
    path('student2/<int:pk>/', StudentDetailView2.as_view(), name='studentdetail2'),
    path('student3/<int:pk>/', StudentDetailView3.as_view(), name='studentdetail3'),


]
