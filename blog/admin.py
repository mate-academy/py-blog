from django.contrib import admin
from .models import User, Post, Commentary
from django.contrib.auth.models import Group


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", ]
    list_filter = ["username", ]
    search_fields = ["username", ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", ]
    list_filter = ["title", ]
    search_fields = ["title", ]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", ]
    list_filter = ["created_time", ]
    search_fields = ["user", "created_time", ]


admin.site.unregister(Group)
