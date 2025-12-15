from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    search_fields = ["title", "content"]
    list_filter = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    search_fields = ["content"]
    list_filter = ["user", "post", "created_time"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
