from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from blog.models import Post, Commentary

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username"]
    list_filter = ["username", "is_active"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["owner"]
    list_filter = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    list_filter = ["user", "created_time"]

admin.site.unregister(Group)
