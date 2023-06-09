from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post


def index(request, page=1):
    posts = Post.objects.select_related("owner")
    paginator = Paginator(posts, 2)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context=context)
