from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from blog.models import Post, Commentary

User = get_user_model()

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)
