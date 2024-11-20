from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Commentary, Post

admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["content", ]
    search_fields = ["post__title", ]


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_filter = ["username", ]
    search_fields = ["username", ]
    add_fieldsets = UserAdmin.fieldsets


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["title", ]
    search_fields = ["title", ]
