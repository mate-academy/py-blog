from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import User, Post, Commentary

def index(request: HttpRequest) -> HttpResponse:
    user_count = User.objects.count()
    post_count = Post.objects.count()
    comment_count = Commentary.objects.count()
    posts = Post.objects.annotate(comments_count=Count("comments")).order_by("-created_time")

    context = {
        "user_count": user_count,
        "post_count": post_count,
        "comment_count": comment_count,
        "posts": posts,
    }

    return render(request, "blog/index.html", context=context)
