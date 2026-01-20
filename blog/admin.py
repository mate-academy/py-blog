from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.models import Group


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets[:1] + (
        (("Additional info", {"fields": ("first_name", "last_name",)}),)
    ) + UserAdmin.fieldsets[2:]
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "username",
                        "email",
                    )
                },
            ),
        )
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)


admin.site.register(Commentary)
admin.site.unregister(Group)
