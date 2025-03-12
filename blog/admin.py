from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "content", "created_time")
    list_filter = ("created_time",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    list_filter = ("post",)
    search_fields = ("user",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "password")
    list_filter = ("username",)
    search_fields = ("username", "first_name", "last_name")


admin.site.unregister(Group)
