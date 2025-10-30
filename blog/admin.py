from django.contrib import admin
from django.contrib.auth.models import Group

from blog import models


admin.site.register(models.User)
admin.site.unregister(Group)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author__username", "created_time",)
    search_fields = ("title", "author__username")


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("author__username", "created_time",)
    search_fields = ("content", "author__username")
