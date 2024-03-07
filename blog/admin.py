from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Commentary, Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time"]
    list_filter = ["user", "created_time"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display
    search_fields = ("username", )


admin.site.unregister(Group)
