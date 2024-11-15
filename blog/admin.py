from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary

# Unregister Group model
admin.site.unregister(Group)


# Custom UserAdmin (if you want to customize User model)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")


# Register Post model with filtering and searching
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content", "owner__username")
    list_filter = ("created_time", "owner__username")


# Register Commentary model with filtering and searching
@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time", "content")
    search_fields = ("post__title", "user__username", "content")
    list_filter = ("created_time", "post__title", "user__username")
