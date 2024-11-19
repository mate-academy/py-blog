from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content",)
    list_filter = ("owner",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content",)
    list_filter = ("post",)
    search_fields = ("content",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    list_filter = UserAdmin.list_filter
    search_fields = UserAdmin.search_fields

    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
