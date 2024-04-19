from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.utils.html import format_html

from .models import Post
from .models import Commentary
from .models import User
from django.urls import reverse

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("all_posts",)
    search_fields = ["username", "first_name", "last_name", ]
    list_filter = ["username", ]

    @staticmethod
    def all_posts(obj):
        post_count = obj.post_set.count()
        url = reverse("admin:blog_post_changelist")
        return format_html(
            '<a href="{}?owner__id__exact={}">{}</a>',
            url, obj.id, post_count
        )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time", ]
    search_fields = ["title", "owner", ]
    list_filter = ["title", "created_time", "owner", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post_title", "created_time", ]
    search_fields = ["user", "post_title", ]
    list_filter = ["user", "post", "created_time", ]

    @staticmethod
    def post_title(obj):
        return obj.post.title
