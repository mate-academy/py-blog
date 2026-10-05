from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner", "created_time")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content")
    search_fields = ("user", "content")
    list_filter = ("user", "created_time")


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
