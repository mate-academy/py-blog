from blog.models import Post, Commentary
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username"]
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("owner", "title", "content", "created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("user",)
