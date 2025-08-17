from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_time")
    list_filter = ("created_time",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
    )
    ordering = ("last_name",)
    search_fields = ("username", "first_name", "last_name", "email",)


admin.site.unregister(Group)
