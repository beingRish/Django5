from django.contrib import admin
from myapp.models import Profile, Page, Like, Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['likes']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']