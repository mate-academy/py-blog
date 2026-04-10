from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post

admin.site.unregister(Group)


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner"]
    search_fields = ["title", "owner__username"]
    list_filter = ["owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "user"]
    search_fields = ["content", "user__username"]
    list_filter = ["post", "user"]
