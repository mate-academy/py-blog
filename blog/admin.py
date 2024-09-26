from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["created_time", "content", "owner"]
    search_fields = ["title", "content"]
    list_filter = ["title", "owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["pk", "created_time", "content", "post"]
    search_fields = ["content", ]
    list_filter = ["post", ]
