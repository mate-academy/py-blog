from django.contrib import admin
from django.contrib.auth.models import Group, User

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time",)
    list_filter = ("owner",)
    search_fields = ["content"]
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "created_time",)
    list_filter = ("post", "user")
    list_select_related = ("post",)
    search_fields = ["content"]
    ordering = ("-created_time",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name",)
    ordering = ("username",)


admin.site.unregister(Group)
