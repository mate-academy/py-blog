from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import User, Commentary, Post
from django.contrib.auth.models import Group


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time"]
    list_filter = ["created_time", ]
    search_fields = ["content", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_time"]
    list_filter = ["title", ]
    search_fields = ["title", ]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.unregister(Group)
