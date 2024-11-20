from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


# admin_a, asd4891
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "owner", "created_time", "comment_count"]
    search_fields = ["title"]
    list_filter = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "post", "user"]
    search_fields = ["content"]
    list_filter = ["user"]


admin.site.unregister(Group)
