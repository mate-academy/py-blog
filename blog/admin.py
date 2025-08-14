from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
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
    list_display = ["title", "short_content", "created_time"]
    search_fields = ("title", "owner.username",)
    list_filter = ("owner", "created_time", )

    def short_content(self, obj):
        return obj.content[:25]
    short_content.short_description = "Content"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["get_post_title", "short_content", "created_time"]
    search_fields = ("content", )
    list_filter = ("created_time", "user", "post", )

    def get_post_title(self, obj):
        return obj.post.title
    get_post_title.short_description = "Post Title"

    def short_content(self, obj):
        return obj.content[:20]
    short_content.short_description = "Content"


admin.site.unregister(Group)
