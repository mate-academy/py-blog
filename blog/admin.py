from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "email", "first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = [
        "title",
        "owner__username",
        "owner__email",
        "owner__first_name",
        "owner__last_name"
    ]
    list_filter = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = [
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
        "post__title",
        "content"
    ]
    list_filter = ["user", "post", "created_time"]


admin.site.unregister(Group)
