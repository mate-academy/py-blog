from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary

admin.site.unregister(Group)


admin.site.register(Post)
admin.site.register(Commentary)
