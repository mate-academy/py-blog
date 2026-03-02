from django.contrib import admin

from blog.models import Post, Commentary, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_time')
    search_fields = ('title', 'content')
    list_filter = ('created_time',)

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_time')
    search_fields = ('content',)
    list_filter = ('created_time',)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    search_fields = ('username', 'email')
