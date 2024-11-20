from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary


admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_filter = ["is_staff", "is_superuser"]
    search_fields = ["username", "email"]


admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_filter = ["owner"]
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)


class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ["user", "post"]
    search_fields = ["content"]


admin.site.register(Commentary, CommentaryAdmin)
