from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary

admin.site.register(User)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "comments_count"]
    search_fields = ["title",]
    list_filter = ["owner",]

    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = "Comments"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    search_fields = ["content"]
    list_filter = ["created_time"]


admin.site.unregister(Group)

