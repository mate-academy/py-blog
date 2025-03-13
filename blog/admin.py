from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


# from django.contrib import admin
# from .models import Article, Comment
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'author', 'created_at')
#     search_fields = ('title', 'author__username')
#     list_filter = ('created_at',)
#     ordering = ('-created_at',)
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'article', 'author', 'created_at')
#     search_fields = ('article__title', 'author__username')
#     list_filter = ('created_at',)
