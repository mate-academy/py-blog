from django.contrib import admin
from blog.models import User, Post, Commentary
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Commentary)
