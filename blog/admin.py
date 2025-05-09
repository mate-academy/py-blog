from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Commentary, User


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time",)
    search_fields = ("title", "owner",)
    list_filter = ("created_time" ,"owner",)


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]


admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
