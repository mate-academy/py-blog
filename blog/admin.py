from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)
admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["owner", "created_time"]
    ordering = ["owner", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["display_content", "user", "post"]
    list_filter = ["user", "post"]
    ordering = ["user", "post"]

    def display_content(self, obj):
        if len(obj.content) > 20:
            return obj.content[:20] + "..."
        else:
            return obj.content

    display_content.short_description = "Content"
