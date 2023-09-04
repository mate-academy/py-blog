from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)
