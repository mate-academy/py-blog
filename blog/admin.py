from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


@admin.register(Post)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("owner", "title", "created_time",)
    list_filter = ("owner", "created_time", "title",)


admin.site.register(Commentary)
admin.site.register(User)
admin.site.unregister(Group)
