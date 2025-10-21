from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
