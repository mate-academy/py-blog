from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from blog.models import Post, Commentary


def index(request):
    posts = Post.objects.all().select_related(
        "owner"
    ).order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    paginator.page(paginator.num_pages)

    context = {
        "paginator": paginator,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "post_list": page_obj.object_list,
    }

    return render(request, "blog/index.html", context=context)


def post_detail_retrieve_view(request, *args, **kwargs):
    post = Post.objects.select_related("owner").get(**kwargs)
    commentaries = post.commentaries.all().select_related("user")
    context = {"post": post, "commentaries": commentaries}
    return render(request, "blog/post_detail.html", context=context)


@login_required
def commentary_create_view(request, *args, **kwargs):
    if request.method == "POST":
        Commentary.objects.create(
            user_id=request.user.id,
            post_id=kwargs["pk"],
            content=request.POST.get("comment"),
        )

        return redirect("blog:post-detail", pk=kwargs["pk"])
