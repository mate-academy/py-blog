from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.register(Post)
admin.site.register(Commentary)
