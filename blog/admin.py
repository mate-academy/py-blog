from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    User,
    Post,
    Commentary,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["title", "owner", "created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "post", "created_time"]


admin.site.register(User)
admin.site.unregister(Group)
