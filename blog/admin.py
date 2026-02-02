from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Commentary, Post

admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "post", "created_time"]
    list_display_links = [
        "comment",
    ]
    list_filter = [
        "user",
    ]
    search_fields = ["content", "post__title"]

    @admin.display(description="Comment")
    def comment(self, obj):
        return obj.__str__()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_display_links = [
        "title",
    ]
    list_filter = [
        "owner",
    ]
    search_fields = [
        "title",
    ]


@admin.register(User)
class User(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name")}),
    )
