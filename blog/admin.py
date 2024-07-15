from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner__username")
    list_filter = ("created_time",)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("user__username", "post__title")
    list_filter = ("created_time",)
