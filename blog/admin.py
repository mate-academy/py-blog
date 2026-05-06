from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Commentary, User
from django.contrib.auth.models import Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)
    list_display = ("title", "owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("user", "post",)
    list_display = ("user", "post", "short_content", "created_time")


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
