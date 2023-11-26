from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


# Register models
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "owner", "content",)
    list_filter = ("title", "owner", "created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("post", "user", "content",)
    list_filter = ("post", "user", "created_time",)


admin.site.register(User)

# Unregister group
admin.site.unregister(Group)
