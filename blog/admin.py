from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name"]


admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)
