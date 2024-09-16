from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "email")}),
    )


admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)