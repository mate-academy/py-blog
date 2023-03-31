from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "created_time", "owner"]
    list_filter = ["owner__username", "created_time"]


class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["post"]
    list_display = ["user", "post", "created_time"]
    list_filter = ["user__username", "post__title"]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)

admin.site.unregister(Group)
