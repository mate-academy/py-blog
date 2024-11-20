from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")
    search_fields = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    search_fields = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "created_time")
    list_filter = ()
    search_fields = ()
