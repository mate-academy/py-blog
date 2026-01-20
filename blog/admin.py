from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


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
                        "email",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time", )
    search_fields = ("title", )
    list_filter = ("owner", "created_time", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post_title", "content", "created_time", )
    search_fields = ("post__title", )
    list_filter = ("user", "created_time", )

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = "Post title"


admin.site.unregister(Group)
