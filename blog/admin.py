from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Commentary, User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
<<<<<<< HEAD
class UserAdmin(UserAdmin):
=======
class CustomUserAdmin(UserAdmin):
>>>>>>> 28d22212fac2cd0fb6e6ef5ce019e7f245630d2a
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_time')
    search_fields = ('title', 'content')

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_time")
<<<<<<< HEAD
    search_fields = ("post", "user__username")
=======
    search_fields = ("post", "user__username")
>>>>>>> 28d22212fac2cd0fb6e6ef5ce019e7f245630d2a
