from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    search_fields = ["username", "first_name", "last_name"]
    list_filter = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    search_fields = ["title"]
    list_filter = ["created_time", "owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "user", "post", "created_time"]
    search_fields = ["user__username", "post__title"]
    list_filter = ["user", "post"]
