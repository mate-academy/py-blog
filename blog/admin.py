from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name"
    )
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("content",)
    list_filter = ("user", "post", "created_time")


admin.site.unregister(Group)
