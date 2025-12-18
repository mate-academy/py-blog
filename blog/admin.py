from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner", "created_time", "title")
    list_filter = ("owner", "created_time", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user", "created_time", "post")
    list_filter = ("user", "created_time", "post")


admin.site.unregister(Group)
