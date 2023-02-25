from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Personal info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email"
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    search_fields = ("owner__username", "title")
    search_help_text = "Specify post title or owner's username"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "created_time", "content", "user")
    search_fields = ("user__username", "post__title")
    search_help_text = "Specify post title or username"
