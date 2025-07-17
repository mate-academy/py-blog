from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Commentary, User


admin.site.unregister(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_time']
    search_fields = ['title', 'owner__username']
    list_filter = ['created_time']

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_time']
    search_fields = ['content', 'user__username']
    list_filter = ['created_time']

admin.site.register(User)
