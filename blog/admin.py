from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


admin.site.site_header = "My Awesome Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Hello, boss"

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "short_content", "created_time")

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    short_content.short_description = "short content"

    list_filter = ("created_time",)
    search_fields = ("title", "owner__first_name", "owner__last_name")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post_title", "short_content", "created_time")

    def get_queryset(self, request):
        qr = super().get_queryset(request)
        return qr.select_related("post")

    def post_title(self, obj):
        return obj.post.title

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    short_content.short_description = "short content"

    post_title.short_description = "Post title"

    list_filter = ("created_time",)
    search_fields = ("user__first_name", "user__last_name", "post__title")


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
