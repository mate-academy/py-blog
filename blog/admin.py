from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["owner", "title"]
    search_fields = ["title"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "post"]
    search_fields = ["content"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
