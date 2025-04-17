from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "email")
    list_filter = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("owner", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("created_time", )
    list_filter = ("content", )


admin.site.unregister(Group)