from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "date_joined"
    )
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("is_active", "is_staff")


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_display = ("post", "user", "created_time")
