from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Commentary, User, Post


admin.site.register(User)
admin.site.register(Commentary)
admin.site.register(Post)
admin.site.unregister(Group)
