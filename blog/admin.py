from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(User)
class DriverAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time",)
    search_fields = ("owner", "title",)
    list_filter = ("owner", "created_time",)


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content",)
    search_fields = ("user", "post",)
    list_filter = ("user", "created_time",)


admin.site.unregister(Group)
