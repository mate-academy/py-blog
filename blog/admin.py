from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "owner", ]
    search_fields = ["owner", "title", "content", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "user", ]
    search_fields = ["user", "post", "content"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ["last_login", "is_active", "date_joined", ]
    search_fields = ["username", "email"]


admin.site.unregister(Group)
