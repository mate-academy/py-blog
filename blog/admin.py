from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner__username")
    list_filter = ("created_time",)
    ordering = ("-created_time",)

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("user__username", "post__title")
    list_filter = ("created_time",)
    ordering = ("-created_time",)

@admin.register(get_user_model())
class AdminUser(UserAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff",)
    ordering = ("username",)

admin.site.unregister(Group)