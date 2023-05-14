from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")
    list_filter = ("username",)
    search_fields = ("username", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner")
    list_filter = ("title", )
    search_fields = ("title", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "content")
    list_filter = ("user",)
    search_fields = ("user",)
