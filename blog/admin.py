from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["post", "user"]
    search_fields = ["content"]


admin.site.register(User)
admin.site.unregister(Group)
