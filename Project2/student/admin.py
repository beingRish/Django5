from django.contrib import admin
from student.models import Profile, Result

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'email', 'city']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'stu_class', 'marks']