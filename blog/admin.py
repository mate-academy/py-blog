from django.contrib import admin
from django.contrib.auth.models import Group

from blog import models


admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.Commentary)
admin.site.unregister(Group)
