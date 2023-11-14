from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', "is_staff"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_time']


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_time', 'content']
