from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ["username"]
    search_fields = ("username", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ["-created_time"]
    list_filter = ("owner", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    ordering = ["-created_time"]
    list_filter = ("user", )
