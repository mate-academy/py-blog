from blog.models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
