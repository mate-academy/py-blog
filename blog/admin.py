from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, User, Commentary


admin.site.unregister(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "owner"]
    search_fields = ("title", "content", "owner__username")

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["created_time", "user", "post"]
    search_fields = ("content", "user__username", "post__title")


@admin.register(User)
class UserAdmin(UserAdmin):
    pass