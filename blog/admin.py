from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["owner", "created_time"]
    search_fields = ["title", "content"]
    list_display = ["owner", "title", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "created_time"]
    search_fields = ["post", "content"]
    list_display = ["user", "post", "created_time"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "username"]


admin.site.unregister(Group)
