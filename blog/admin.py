from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class OwnerAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name")
        }),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    search_fields = ["owner", "title", ]
    list_filter = ["title", "created_time", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]
    search_fields = ["user", "post", ]
    list_filter = ["user", "post", "created_time", ]


admin.site.unregister(Group)
