from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(Post)
admin.site.register(Commentary)
