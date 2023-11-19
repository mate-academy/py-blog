from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")
    list_filter = (
        ("is_staff", admin.BooleanFieldListFilter),
        ("email", admin.EmptyFieldListFilter),
    )
    ordering = ["first_name", "last_name"]
    search_fields = ("username", "first_name", "last_name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")
    list_filter = (
        "owner",
        "created_time",
    )
    search_fields = ("owner__username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user", "post", "created_time")
    search_fields = (
        "user__username",
        "post__title",
    )


admin.site.unregister(Group)
