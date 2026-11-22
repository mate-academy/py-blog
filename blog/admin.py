from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_time")
    list_filter = ("title", )
    search_fields = ("title", )


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "content", "created_time")
    list_filter = ("post", )
    search_fields = ("content",)


admin.site.unregister(Group)
