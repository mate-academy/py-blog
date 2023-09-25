from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, User, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user", "post"]


admin.site.unregister(Group)
