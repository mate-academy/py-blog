from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "post", "created_time",)
    list_filter = ("created_time",)


admin.site.register(get_user_model())
admin.site.unregister(Group)
