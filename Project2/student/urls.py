from django.urls import path
from student.views import all_data, single_data, student_form_view, teacher_form_view, login, address, demo_form, reg_success

urlpatterns = [
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
    path('student-register/', student_form_view, name='student_form_view'),
    path('teacher-register/', teacher_form_view, name='teacher_form_view'),
    path('login/', login, name='login'),
    path('address/', address, name='address'),
    path('demo-form/', demo_form, name='demo_form'),
    path('success/', reg_success, name='reg_success'),
]
