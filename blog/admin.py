from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import Post, Commentary


User = get_user_model()


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "created_time")
    search_fields = ("title", "owner__username")
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_time")
    search_fields = ("user__username", "post__title")
    list_filter = ("created_time",)
