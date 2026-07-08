from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Commentary, Post

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "first_name", "last_name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("owner", "created_time")
    date_hierarchy = "created_time"

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    search_fields = ("created_time", "content")
    list_filter = ("user", "created_time", "post")
