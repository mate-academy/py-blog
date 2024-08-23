from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")

    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context=context)
