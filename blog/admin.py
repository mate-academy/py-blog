from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner__username", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("post__title", )
