from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Commentary)
admin.site.register(User)

admin.site.unregister(Group)