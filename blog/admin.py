from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Comment


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "post", "created_time")
    search_fields = ("text",)
    list_filter = ("post",)


admin.site.unregister(Group)
