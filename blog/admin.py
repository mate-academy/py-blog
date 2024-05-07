from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["title", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "user",
        "created_time",
    ]
    list_filter = [
        "user",
    ]


admin.site.register(User, UserAdmin)
