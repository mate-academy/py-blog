from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = (
        "username",
        "first_name",
        "last_name",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "date_joined",
        "last_login"
    )


class AdminFormattedCreatedTimeMixin:
    @admin.display(
        description="Created time",
        ordering="created_time"
    )
    def admin_created_time(self, obj):
        return obj.created_time.strftime("%d.%m.%Y, %H:%M")


@admin.register(Post)
class PostAdmin(AdminFormattedCreatedTimeMixin, admin.ModelAdmin):
    search_fields = ("title", "content", "commentaries__content")
    list_filter = ("created_time", "owner", )
    list_display = ("admin_created_time", "owner", "title")


@admin.register(Commentary)
class CommentaryAdmin(AdminFormattedCreatedTimeMixin, admin.ModelAdmin):
    search_fields = ("user", "content", )
    list_filter = ("user", "post", "created_time", )
    list_display = ("admin_created_time", "user", "post")
