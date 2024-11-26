from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "content", ]
    list_filter = ["owner", "title", "created_time", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["content", "created_time", ]
    list_filter = ["user", "post", "created_time", ]


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
