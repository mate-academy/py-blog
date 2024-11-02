from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, User, Commentary

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created_time", "owner", "title", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "post", "user", "content", )
    list_filter = ("created_time",)
    search_fields = ("user__username", "post__title", "content", )
