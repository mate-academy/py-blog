from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Post


def index(request):
    posts_list = Post.objects.select_related("owner").all()
    page = request.GET.get("page", 1)
    paginator = Paginator(posts_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts
    }

    return render(request, "index.html", context=context)
