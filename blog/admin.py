from django.contrib import admin

from django.contrib.auth.models import Group

from .models import User, Post, Commentary


# @admin.register(User)
# class User(UserAdmin):
#


@admin.register(Post)
class Post(admin.ModelAdmin):
    model = Post
    list_filter = ["owner", "title"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ["content"]
    list_filter = ["user", "post"]
    # search_fields = ["created_time"]
    model = Commentary


admin.site.register(User)

admin.site.unregister(Group)
