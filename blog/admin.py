from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.register(Commentary)
admin.site.register(Post)
admin.site.unregister(Group)
