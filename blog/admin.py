from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (("Additional info"), {"fields": ("first_name", "last_name")}),)


admin.site.register(Post)
admin.site.register(Commentary)

admin.site.unregister(Group)
