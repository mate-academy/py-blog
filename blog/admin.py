from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]
    list_filter = ["user", "post"]
    search_fields = ["post", "created_time", "content"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
