from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner",)
    search_fields = ("title",)
    list_display = ("title", "owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("post", "user",)
    list_display = ("__str__", "user", "post",)
