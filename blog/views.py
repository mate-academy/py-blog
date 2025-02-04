from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("created_time")
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "page_obj": page_obj,
        "is_paginated": paginator.num_pages > 1
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post


@login_required
def send_commentary(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        commentary = request.POST.get("commentary", "")
        Commentary.objects.create(user_id=request.user.id,
                                  post_id=pk,
                                  content=commentary)

        return redirect(reverse("blog:post-detail", kwargs={"pk": pk}))
    else:
        return redirect(reverse("blog:post-detail", kwargs={"pk": pk}))
