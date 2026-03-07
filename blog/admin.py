from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Comment

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name",
                    "last_name", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active")
    ordering = ("username",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "content", "created_time", "comments_count")
    search_fields = ("author__username", "title", "content")
    list_filter = ("author", "created_time")
    ordering = ("-created_time",)

    def comments_count(self, obj):
        return obj.comments.count()


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_date", "short_content")
    search_fields = ("author__username", "post__title", "text")
    list_filter = ("author", "created_date")
    ordering = ("-created_date",)

    def short_content(self, obj):
        return (obj.text[:50] + '...') \
            if len(obj.text) > 50 else obj.text

    short_content.short_description = 'Content'


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
