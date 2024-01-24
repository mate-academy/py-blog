from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    list_filter = ("title", "created_time")
    search_fields = ("title", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "user")
    list_filter = ("created_time", "user")
    search_fields = ("created_time", "user")


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
