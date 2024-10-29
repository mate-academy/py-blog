from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", )
    search_fields = ("title", )

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "post", "user", )

@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "first_name", "last_name", )

admin.site.unregister(Group)
