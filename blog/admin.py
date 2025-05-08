from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from .models import Post, Comment, User

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("title", "owner__username")


admin.site.register(User, UserAdmin)
admin.site.register(Comment)
admin.site.unregister(Group)
admin.site.register(Post, PostAdmin)

