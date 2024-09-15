from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content",)
    list_filter = ("created_time", "owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("created_time", "user", "post")
