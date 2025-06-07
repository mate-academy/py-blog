from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdministrator(UserAdmin):
    list_filter = UserAdmin.list_filter + ("username", 'first_name', 'last_name')
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('first_name', 'last_name', 'email')})
    ),
