from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "email",)
    list_filter = ("username", "email",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title",)

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username",)
    list_filter = ("user__username", "post__title",)


admin.site.unregister(Group)