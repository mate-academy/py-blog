from django.contrib import admin

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", )
    list_filter = ("owner__username", )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("owner")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", )


@admin.register(Commentary)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("created_time", )
    ordering = ("post__title", )
    list_filter = ("user__username", )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("user").select_related("post")
