from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("title", "created_time")
    search_fields = ("title", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
