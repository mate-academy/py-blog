from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import CommentForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by("-created_time").annotate(
        comment_count=Count("comments")
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", "")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": posts,
        "is_paginated": True,
        "paginator": paginator,
        "page_obj": page_obj,
    }
    return render(request, template_name="blog/index.html", context=context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context=context)
