from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'created_time',)
    list_filter = ('created_time', 'owner', 'title',)
    search_fields = ('title',)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_time', 'content',)
    list_filter = ('user', 'post',)
    search_fields = ('user',)


admin.site.unregister(Group)