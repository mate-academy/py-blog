from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Post, Commentary, User


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content")
    list_filter = ("owner",)
    search_fields = ("title", "content",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "created_time")
    list_filter = ("user",)
    search_fields = ("content",)


admin.site.unregister(Group)
