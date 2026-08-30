from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content")


admin.site.register(Post, PostAdmin)


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_time")
    list_filter = ("created_time",)
    search_fields = ("user", "content")


admin.site.register(Commentary, CommentaryAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password")
    search_fields = ("username", "email", "password")


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
