from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["owner", "title", "created_time", ]
    search_fields = ["owner__username", "title", "content", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "post", "created_time", ]
    search_fields = ["user__username", "post__title", "content", ]
