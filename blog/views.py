from django.core.paginator import Paginator
from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from .models import Post
from .forms import CommentaryForm


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator
    }
    return render(request,
                  "blog/index.html",
                  context=context)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.commentary_set.all().order_by("created_time")

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.post = post
                new_comment.save()
                return redirect("blog:post-detail", pk=post.pk)
        else:
            form = CommentaryForm()
            form.add_error(None,
                           "Musisz być zalogowany, aby dodać komentarz.")
    else:
        form = CommentaryForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })
