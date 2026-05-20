from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary

admin.site.unregister(Group)


class CommentaryInline(admin.TabularInline):
    model = Commentary
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def comments_count(self, obj):
        return obj.commentaries.count()

    list_display = ("id", "title", "created_time", "owner", "comments_count")
    inlines = [CommentaryInline]
    search_fields = ("title",)
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ("id", "user", "created_time", "post")
    search_fields = ("user__username", "post__title")
    list_filter = ("created_time", "user")


@admin.register(User)
class CustomUserAdmin(
    UserAdmin
):  # pyright: ignore[reportUntypedBaseClass, reportGeneralTypeIssues]
    list_display = (
        "id",
        "username",
        "email",
        "is_staff",
        "is_active",
        "first_name",
        "last_name",
    )
    search_fields = ("username", "email", "first_name", "last_name")
