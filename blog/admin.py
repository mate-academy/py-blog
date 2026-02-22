from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    class Meta:
        search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "content", "created_time")
    list_filter = ("title", "created_time")
    search_fields = ("title",)

    def short_content(self):
        return self.content[:75] + "..."


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    list_filter = ("content", "created_time",)
    search_fields = ("content",)


try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass