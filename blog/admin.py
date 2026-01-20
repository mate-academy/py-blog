from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time",)
    search_fields = ("title",)
    list_filter = ("owner__username",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time",)
    search_fields = ("user__username",)
    list_filter = ("post__title",)


admin.site.unregister(Group)
