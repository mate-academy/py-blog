from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "content", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("owner__username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_time")
    list_filter = ("user", "created_time")
    search_fields = ("user__username", )


admin.site.register(User, UserAdmin)
