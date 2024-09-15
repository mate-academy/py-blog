from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import site

from blog.models import Commentary, Post, User


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "content"]
    list_filter = ["user"]
    search_fields = ["content"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner"]
    list_filter = ["title"]
    search_fields = ["title"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]
    list_filter = ["username"]
    search_fields = ["username"]


admin.site.unregister(Group)

site.disable_action("delete_selected")
