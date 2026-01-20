from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post, Commentary

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Поля, которые будут видны в списке
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # фильтры сбоку
    search_fields = ('username', 'first_name', 'last_name', 'email')  # поиск
    ordering = ('username',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_time')
    list_filter = ('owner', 'created_time')  # фильтры по владельцу и дате
    search_fields = ('title', 'content')     # поиск по заголовку и содержимому
    ordering = ('-created_time',)

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('post', 'owner', 'created_time', 'content')
    list_filter = ('owner', 'created_time', 'post')  # фильтры
    search_fields = ('content', 'owner__username', 'post__title')  # поиск по тексту, автору и посту
    ordering = ('-created_time',)