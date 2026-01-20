from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", ]


admin.site.unregister(Group)
