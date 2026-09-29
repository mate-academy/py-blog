from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Tag, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("tags",)
    search_fields = ("title", "content")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content")
