from django.contrib.auth.models import Group
from django.contrib import admin

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    search_fields = ("title", "owner")
    list_filter = ("owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("user", "post")
    list_filter = ("user", "created_time")
