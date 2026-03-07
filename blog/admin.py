from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name",
                    "last_name", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active")
    ordering = ("username",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    search_fields = ("owner__username", "title", "content")
    list_filter = ("owner", "created_time")
    ordering = ("-created_time",)

    def comments_count(self, obj):
        return obj.comments.count()


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    search_fields = ("user__username", "post__title", "content")
    list_filter = ("user", "created_time")
    ordering = ("-created_time",)

    def short_content(self, obj):
        return (obj.content[:50] + '...') \
            if len(obj.content) > 50 else obj.content

    short_content.short_description = 'Content'


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)
