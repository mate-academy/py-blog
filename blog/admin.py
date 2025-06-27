from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from blog.models import CustomUser, Post, Commentary


admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)


admin.site.register(Commentary)
