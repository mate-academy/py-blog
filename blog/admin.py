from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time", ]
    list_filter = ["created_time", ]
    search_fields = ["owner__username", "title"]


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time", ]
    list_filter = ["created_time", ]
    search_fields = ["user__username", ]


admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
