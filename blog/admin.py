from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("owner__username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user__username", "post__title")
    search_fields = ("user__username", "content", "post__title")


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email")
    list_filter = ("username",)
    search_fields = ("username",)
    ordering = ("username",)


admin.site.unregister(Group)
