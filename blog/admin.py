from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


admin.site.register(User)
admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content",)
    list_filter = ("user", "post",)
    search_fields = ("content", "user",)
    ordering = ("created_time",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content")
    list_filter = ("owner", "title")
    search_fields = ("content", "owner")
    ordering = ("created_time",)
