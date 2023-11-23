from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    # list_display = UserAdmin.list_display
    # fieldsets = UserAdmin.fieldsets
    list_filter = ["first_name", ]
    search_fields = ["username", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_time", "content", "owner", ]
    list_filter = ["created_time", ]
    search_fields = ["owner", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time", "post", "content", ]
    list_filter = ["created_time", ]
    search_fields = ["user", ]
