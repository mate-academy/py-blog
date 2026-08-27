from django.contrib import admin
from blog.models import Post, User, Commentary
from django.contrib.auth.models import Group


admin.site.register(User)
admin.site.register(Commentary)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("owner",)
