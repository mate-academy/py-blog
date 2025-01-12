from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "content",
        "created_time",
    ]
    search_fields = (
        "title",
        "created_time",
    )


# admin.site.unregister(Group)
