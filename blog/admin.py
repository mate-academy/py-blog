from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class BlogUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time")
    list_filter = ("created_time", "author")
    search_fields = ("title", "content")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_time", "short_content")
    list_filter = ("created_time", "author")
    search_fields = (
        "author__username",
        "text",
    )

    @admin.display(description="Content Preview")
    def short_content(self, obj):
        if len(obj.content) > 50:
            return f"{obj.content[:50]}..."
        return obj.content
