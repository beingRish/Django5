from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'pass_date', 'admission_date']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'empnum', 'city', 'salary', 'join_date']

