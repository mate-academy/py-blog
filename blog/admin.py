from django.contrib import admin


from django.contrib.auth.admin import UserAdmin as MyUserAdmin


from django.contrib.auth.models import Group


from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(MyUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("owner__username", "title",)
    list_filter = ("owner__username",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("post__title",)
    list_filter = ("created_time",)


admin.site.unregister(Group)
