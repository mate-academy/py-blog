from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("created_time",)
    list_display = ("id", "owner", "title", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("user", "post")
    list_display = ("id", "user", "post", "content")
    search_fields = ("user", "post")


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
