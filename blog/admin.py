from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import (
    User,
    Post,
    Commentary,
)


    

admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", )
    search_fields = ("username", )
    list_filter = ("username", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", )
    search_fields = ("title", "owner", )
    list_filter = ("title", "owner", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post__title", "user", )
    search_fields = ("post__title", "user", )
    list_filter = ("post__title", "user", )
