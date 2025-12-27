from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Comment, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "content", "created_time")
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "content", "created_time")
    list_filter = ("author__username",)
    search_fields = ("content",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    list_filter = UserAdmin.list_filter
    search_fields = UserAdmin.search_fields
