from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)
    list_filter = ("created_time", "owner__username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("username", "created_time")
    search_fields = ("content",)
    list_filter = ("user", "created_time")

    def username(self, obj):
        return obj.user.username


admin.site.unregister(Group)
