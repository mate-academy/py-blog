from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary

admin.site.unregister(Group)
admin.site.register(Post)
admin.site.register(Commentary)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "email"]
    list_display = ("username", "email",)
    list_filter = ("is_staff", )

