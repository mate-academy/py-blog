from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Commentary, User


class CommentaryInline(admin.TabularInline):
    model = Commentary
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "created_time",
    ]
    list_filter = [
        "owner",
        "created_time",
    ]
    search_fields = [
        "title",
        "content",
    ]
    inlines = [CommentaryInline]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "created_time",
    ]
    list_filter = [
        "user",
        "created_time",
    ]
    search_fields = ["content"]


admin.site.register(User, UserAdmin)
