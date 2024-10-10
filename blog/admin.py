from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in User._meta.fields
    ]  # Lists all fields in User model


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Post._meta.fields
    ]  # Lists all fields in Post model
    list_filter = ["owner", "created_time"]
    search_fields = ["title", "content"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Commentary._meta.fields
    ]  # Lists all fields in Commentary model
    list_filter = ["user", "created_time", "post__title"]
    search_fields = ["content"]
