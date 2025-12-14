from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Post, Commentary


User = get_user_model()

try:
    admin.site.unregister(Group)
except Exception:
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff",
                    "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time", "comments_count")
    search_fields = ("title", "content", "owner__username", "owner__email")
    list_filter = ("created_time", "owner")
    date_hierarchy = "created_time"
    ordering = ("-created_time",)

    def comments_count(self, obj):
        return obj.commentaries.count()
    comments_count.short_description = "Comments"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("short_content", "user", "post", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_time", "user")
    ordering = ("-created_time",)

    def short_content(self, obj):
        return (obj.content[:75] + "...") if len(obj.content) > 75 \
            else obj.content
    short_content.short_description = "Comment"
