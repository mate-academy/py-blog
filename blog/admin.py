from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")
    search_fields = ("username", )
    list_filter = ("username", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title",)
    list_filter = ("owner", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user", "post")


admin.site.unregister(Group)
