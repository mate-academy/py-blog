from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["title", "owner", "created_time"]
    search_fields = ["title", "owner", "created_time"]
    raw_id_fields = ("owner",)
    date_hierarchy = "created_time"
    ordering = ["-created_time"]


admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "post", "created_time"]
    search_fields = ["user", "post", "created_time"]
