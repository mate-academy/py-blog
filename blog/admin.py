from django.contrib import admin
from blog.models import User, Post, Commentary
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner", "title", "created_time", )
    search_fields = ("owner", "title", "created_time", )


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_filter = ("user", "post", )
    search_fields = ("user, post", )


admin.site.unregister(Group)
