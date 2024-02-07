from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time", ]
    list_filter = ["owner", ]
    search_fields = ["title", ]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
