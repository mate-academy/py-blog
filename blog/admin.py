from django.contrib import admin

from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(Post)
class Post(admin.ModelAdmin):
    model = Post
    list_filter = ["owner", "title"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ["content"]
    list_filter = ["user", "post"]
    model = Commentary


admin.site.register(User)

admin.site.unregister(Group)
