from django.contrib import admin

from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner")
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "created_time")
    search_fields = ("content", "user")
    list_filter = ("user__username",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "is_staff")
    search_fields = ("username", "first_name", "last_name")
