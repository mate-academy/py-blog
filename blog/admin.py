from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("__str__",)
    list_filter = ("username", "is_staff", "date_joined")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("__str__",)
    list_filter = ("owner", "title", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    ...
