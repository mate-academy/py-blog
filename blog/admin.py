from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["owner", "created_time"]
    list_editable = ["title", "content"]
    search_fields = ["owner", "title", "content", "created_time"]
    date_hierarchy = "created_time"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["user", "created_time"]
    list_editable = ["content", ]
    search_fields = ["post", "user", "created_time"]
    date_hierarchy = "created_time"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]
    list_filter = ["username", "email", "first_name", "last_name"]
    list_editable = ["first_name", "last_name"]
    search_fields = ["username", "email", "first_name", "last_name"]


admin.site.unregister(Group)
