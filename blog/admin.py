from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["owner"]
    ordering = ["-created_time"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    ordering = ["-created_time"]
    search_fields = ["post__title", "user__username"]


admin.site.unregister(Group)
