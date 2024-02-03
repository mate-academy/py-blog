from django.conf import settings
from django.contrib import admin
import django.contrib.auth.admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    list_display = ("is_active", "username", "email", "is_superuser")
    list_display_links = ("username",)
    list_filter = ("is_staff",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner__username")
    list_filter = ("created_time",)


class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "user",
    )
    search_fields = ("post__title",)
    list_filter = ("created_time",)


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)
