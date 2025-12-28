from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from blog.models import Comment, Post

admin.site.unregister(Group)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ["author", "post"]
    search_fields = ["author__username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["title"]
    search_fields = ["author__username"]


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_filter = ["username"]
    search_fields = ["first_name"]
