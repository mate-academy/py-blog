from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_time", "owner")
    list_filter = ("owner",)
    search_fields = ("title",)
    sortable_by = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content", "created_time", "user", "post")
    list_filter = ("user",)
    sortable_by = ("created_time",)
    search_fields = ("content",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
