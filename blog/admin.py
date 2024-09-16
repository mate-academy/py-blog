from django.contrib import admin
from django.contrib.auth import get_user_model, models

from blog.models import Post, Commentary


@admin.register(get_user_model())
class AdminUser(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]
    list_filter = ["username"]
    search_fields = ["username", "first_name", "last_name"]


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    search_fields = ["content"]
    list_filter = ["user", "post"]


admin.site.unregister(models.Group)
