from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    search_fields = ["title", "owner"]
    list_filter = ["title", "owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    search_fields = ["user__username", "post__title"]
    list_filter = ["user__username", "post__title", "created_time"]


admin.site.unregister(Group)
