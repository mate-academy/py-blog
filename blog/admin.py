from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


LIST_PER_PAGE = 10


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "title", "short_content", "created_time")
    list_display_links = ("short_content",)
    ordering = ("-created_time",)
    list_per_page = LIST_PER_PAGE
    search_fields = (
        "id",
        "owner__username",
        "title",
        "content",
        "created_time",
    )
    list_filter = ("owner", "created_time")

    def short_content(self, obj):
        return (
            obj.content[:80] + "..." if len(obj.content) > 80 else obj.content
        )

    short_content.short_description = "Content (short)"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "post",
        "short_content",
        "created_time",
    )
    list_display_links = ("short_content",)
    ordering = ("-created_time",)
    list_per_page = LIST_PER_PAGE
    search_fields = ("user__username", "post__title", "content")

    def short_content(self, obj):
        return (
            obj.content[:150] + "..."
            if len(obj.content) > 150
            else obj.content
        )

    short_content.short_description = "Content (short)"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
    )
    ordering = ("username",)
    list_per_page = LIST_PER_PAGE
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )


admin.site.unregister(Group)
