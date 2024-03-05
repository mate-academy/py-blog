from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request):
    all_posts = Post.objects.all().order_by("created_time")
    context = {
        "all_posts": all_posts
    }
    return render(
        request,
        "blog/index.html",
        context=context
    )
