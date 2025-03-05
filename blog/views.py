from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    context = {
        "post_list": post_list
    }
    return render(request, "blog/index.html", context=context)
