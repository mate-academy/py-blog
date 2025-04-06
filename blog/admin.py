from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("content",)
    list_filter = ("created_time", "user")


admin.site.register(User)
