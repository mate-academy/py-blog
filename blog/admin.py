from django.contrib import admin
from django.contrib.auth.models import Group, User

from blog.models import Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title", "created_time", "owner__id")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("post__id", "created_time", "user__id")


admin.site.unregister(Group)
