from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, User, Commentary

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Commentary)

admin.site.unregister(Group)
