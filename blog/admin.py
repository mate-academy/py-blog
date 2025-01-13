from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time", )
    list_filter = ("owner", )
    search_fields = ("title", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("user", )
    search_fields = ("post__title", )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_superuser", "last_login", )
    search_fields = ("username", "email", )
    ordering = ("username", )


admin.site.unregister(Group)
