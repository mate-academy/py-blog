from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner"]
    search_fields = ["owner__username", "title"]


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["user"]
    search_fields = ["post__title", "user__username"]


admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Commentary, CommentaryAdmin)

admin.site.unregister(Group)
