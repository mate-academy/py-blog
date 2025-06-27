from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary

admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "created_time", "post"]
    list_filter = ["user", "created_time",]
    search_fields = ["user__username",]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time",]
    list_filter = ["owner", "created_time",]
    search_fields = ["title", "owner__username",]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
