from blog.models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time", ]
    list_filter = ["created_time", ]
    search_fields = ["title", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time", ]
    list_filter = ["created_time", "user", ]
