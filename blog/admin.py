from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "owner",
        "content",
        "created_time",
    ]
    search_fields = [
        "title",
        "owner",
        "content",
        "created_time",
    ]


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "get_post_count",
        "get_commentary_count",
    ]
    inlines = [PostInline]

    def get_post_count(self, obj):
        return Post.objects.filter(owner=obj).count()

    get_post_count.short_description = "Count of posts"

    def get_commentary_count(self, obj):
        return Commentary.objects.filter(user=obj).count()

    get_commentary_count.short_description = "Count of commentaries"

    search_fields = [
        "username",
        "email",
    ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "content", "created_time"]
    search_fields = ["post", "user", "content"]
