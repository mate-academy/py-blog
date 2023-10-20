from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("post_count",)
    ordering = ("email",)

    @admin.display
    def post_count(self, obj: User) -> int:
        return obj.posts.count()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "comment_count")
    search_fields = ("title",)

    @admin.display()
    def comment_count(self, obj: Post) -> int:
        return obj.commentaries.count()


@admin.register(Commentary)
class Commentary(admin.ModelAdmin):
    list_display = ("id", "user", "post")
    search_fields = ("content__icontains",)
