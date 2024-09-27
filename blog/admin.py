from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


from blog.models import User, Post, Commentary


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                    )
                },
            ),
        )
    )
    filter_horizontal = ()
    search_fields = ("username",)
    list_filter = ("username",)


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "created_time", "owner")
    ordering = ("title",)
    search_fields = ("title",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(ModelAdmin):
    list_display = ("user", "post", "created_time")
    ordering = ("created_time",)
    search_fields = ("user",)
    list_filter = ("created_time",)


admin.site.unregister(Group)
