from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # 5 posts por página

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)
