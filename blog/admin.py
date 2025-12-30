from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username", "email",)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("title", "owner",)
    search_fields = ("title", "owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("user", "post")
    search_fields = ("user", "post",)

admin.site.unregister(Group)