from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Post, Commentary
from .forms import CommentaryForm


def index(request):
    posts = Post.objects.all().order_by("-created_time")

    paginator = Paginator(posts, 5)
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

    comments = Commentary.objects.filter(post=post).order_by("-created_time")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect("blog:post-detail", pk=post.pk)

        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = CommentaryForm()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post_detail.html", context)