from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


@admin.register(Post)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)


admin.site.register(Commentary)
admin.site.unregister(Group)
