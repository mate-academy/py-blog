from blog.models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.fieldsets
    search_fields = ("first_name", "last_name", "username",)
    list_filter = ("first_name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner", "title", "content",)
    list_filter = ("title",)


admin.site.register(Commentary)

admin.site.unregister(Group)
