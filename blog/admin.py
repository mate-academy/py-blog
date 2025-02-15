from django.contrib import admin

from .models import Post, Comment, Commentary
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Commentary)
