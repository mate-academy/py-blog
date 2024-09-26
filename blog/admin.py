from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class User(UserAdmin):
    pass


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["post"]
    search_fields = ["post"]
