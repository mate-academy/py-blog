from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ("first_name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content", "post")
    list_filter = ("user", "post")


admin.site.unregister(Group)
