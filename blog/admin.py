from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary

# Unregister the Group model from the admin interface
admin.site.unregister(Group)

# Define a custom admin class for each model to add filters and search fields
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")  # Display these fields in the list view
    search_fields = ("username",)      # Add a search field for the login attribute

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "created_time")  # Display these fields in the list view
    search_fields = ("owner",)              # Add a search field for the name attribute

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "created_time")  # Display these fields in the list view
    list_filter = ()                         # Add filters for these fields
    search_fields = ()

