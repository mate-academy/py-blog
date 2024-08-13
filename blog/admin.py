from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

@admin.register(User)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display

    fieldsets = UserAdmin.fieldsets


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
