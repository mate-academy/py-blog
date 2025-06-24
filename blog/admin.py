from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["owner", "title", "created_time"]
    list_filter = ["owner", "title", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user", "post"]
    list_filter = ["user", "post"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
