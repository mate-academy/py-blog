from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created_time",)
    search_fields = (
        "title",
        "owner",
    )
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time",)
    list_filter = ("created_time",)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
