from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    ...
