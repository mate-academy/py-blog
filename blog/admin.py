from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import Commentary, Post, User
from django.contrib.auth.models import Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", "owner"]
    search_fields = ["title", "owner__username", "content"]
    list_filter = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "created_time", "user"]
    search_fields = ["user__username", "content"]
    list_filter = ["post", "user", "created_time"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
