from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as MyUserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user", "post")
    list_filter = ("user", "post")


admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
