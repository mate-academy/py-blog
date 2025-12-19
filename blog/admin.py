from django.contrib import admin
from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("created_time", "owner__username")
    search_fields = ("title", "owner__username", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("created_time", )
    search_fields = ("post__title", "user__username")


site.register(User, UserAdmin)
site.unregister(Group)
