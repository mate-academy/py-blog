from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("hobby",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("hobby",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "hobby")}),
    )
    search_fields = ["username", "first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_time", "owner_username"]
    list_filter = ["title", "owner__username", "created_time"]
    search_fields = ["title", "content", "owner__first_name", "owner__last_name", "owner__username"]

    def owner_username(self, obj):
        return obj.owner.username
    owner_username.admin_order_field = "owner__username"
    owner_username.short_description = "Owner"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time", "user_username", "post"]
    list_filter = ["created_time", "user__username"]
    search_fields = ["content", "user__username"]

    def user_username(self, obj):
        return obj.user.username

    user_username.admin_order_field = "user__username"
    user_username.short_description = "User"
