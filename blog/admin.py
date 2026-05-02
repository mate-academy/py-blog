from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, User, Commentary

admin.site.unregister(Group)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "content")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    search_fields = ["title",]
    list_filter = ("owner",)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (UserAdmin.add_fieldsets
                     + (("Additional info",
                         {"fields": ("first_name", "last_name",)}),))
