from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_time",
        "owner",
    ]
    list_filter = ["created_time"]
    search_fields = ["owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        "created_time",
        "user",
    )
    list_filter = ["created_time"]
    search_fields = ["owner"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
