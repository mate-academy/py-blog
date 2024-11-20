from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary
from django.contrib import admin


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username", "first_name", "last_name"]
    list_filter = ["first_name", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", ]
    list_filter = ["owner", "created_time", ]


@admin.register(Commentary)
class CommentsAdmin(admin.ModelAdmin):
    search_fields = ["post__title", ]
    list_filter = ["user", "created_time", ]


admin.site.unregister(Group)
