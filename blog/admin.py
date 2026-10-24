from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content", "owner__username")
    list_filter = ("created_time",)
    list_select_related = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_time",)
    list_select_related = ("user", "post")
