from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ["username", "first_name", "last_name"]
    list_display = ("first_name", "last_name", "username", "email", "is_staff")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["owner", "title", "created_time"]
    list_display = ("owner", "title", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "post", "created_time"]
    list_display = ("user", "post", "created_time")
