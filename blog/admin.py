from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Commentary, Post


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner__username",)
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user__username",)
    list_filter = ("user",)
