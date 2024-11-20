from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["post", "created_time"]
    search_fields = ["post"]
