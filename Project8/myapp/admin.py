from django.contrib import admin
from .models import Student, Candidate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'course']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']