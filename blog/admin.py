from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner", "title"]
    search_fields = ["title", "owner__username"]


admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Commentary)
