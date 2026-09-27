from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.db.models import Count

from blog.models import Commentary, Post, User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "username", "email", "first_name", "last_name", "is_staff",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time", "commentaries_count")
    list_filter = ("owner", "created_time")
    search_fields = ("title", "content")
    date_hierarchy = "created_time"

    def get_queryset(self, request):
        return (
            super().get_queryset(request)
            .select_related("owner")
            .annotate(_commentaries_total=Count("commentaries"))
        )

    @admin.display(description="Commentaries")
    def commentaries_count(self, obj):
        return obj._commentaries_total


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content_excerpt", "user", "post_title", "created_time")
    list_filter = ("user", "created_time")
    search_fields = ("content", "post__title")
    date_hierarchy = "created_time"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user", "post")

    @admin.display(description="Content")
    def content_excerpt(self, obj):
        excerpt = obj.content[:50]
        if len(obj.content) > 50:
            return f"{excerpt}…"
        return obj.content

    @admin.display(description="Post")
    def post_title(self, obj):
        return obj.post.title


admin.site.unregister(Group)
