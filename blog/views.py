from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import CommentaryForm
from blog.models import User, Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    user_count = User.objects.count()
    post_count = Post.objects.count()
    comment_count = Commentary.objects.count()
    post_list = Post.objects.annotate(
        comments_count=Count("comments")
    ).order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "user_count": user_count,
        "post_count": post_count,
        "comment_count": comment_count,
        "post_list": page_obj.object_list,
        "paginator": paginator,
        "is_paginated": paginator.num_pages > 1,
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context=context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    queryset = Post.objects.all().prefetch_related("comments__user")
    post = get_object_or_404(queryset, pk=pk)
    form = CommentaryForm()

    if request.method == "POST":
        if request.user.is_authenticated:

            form = CommentaryForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
            return redirect("blog:post-detail", pk=post.pk)

        else:
            return redirect("login")

    context = {
        "post": post,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context=context)
