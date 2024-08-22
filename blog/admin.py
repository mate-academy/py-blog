from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary

admin.site.unregister(Group)
admin.site.register(Commentary)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["title", "owner", "created_time"]
    search_fields = ["owner", "title"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    list_filter = UserAdmin.list_filter
    add_fieldsets = UserAdmin.add_fieldsets
