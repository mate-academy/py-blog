from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by("-created_time")
    return HttpResponse(posts)
