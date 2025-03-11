from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_time')
    list_filter = ('created_time', 'owner')
    search_fields = ('title', 'owner__username')


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_time')
    list_filter = ('created_time', 'user')
    search_fields = ('content', 'user__username')
