from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import Group

# Відключаємо групи
admin.site.unregister(Group)


# Конфігурація для Post
class PostAdmin(admin.ModelAdmin):
    list_filter = ["author", "created_time"]
    search_fields = ["title", "content"]


# Реєструємо Post з кастомним адміном
admin.site.register(Post, PostAdmin)

# Реєструємо Comment звичайним способом
admin.site.register(Comment)
