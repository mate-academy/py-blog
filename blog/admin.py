from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", "owner"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "created_time", "user"]
    list_filter = ["post"]
    search_fields = ["content"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
