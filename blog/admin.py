from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Model

from blog.models import Post, Commentary, User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    pass
