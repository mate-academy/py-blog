from blog.models import Post, Commentary, User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner", "title"]
    search_fields = ["owner", "title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["post"]
    search_fields = ["post", "user"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
