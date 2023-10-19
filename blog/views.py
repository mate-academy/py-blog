from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, Commentary



def index(request:HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    commentaries = Commentary.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)


    context = {
        "posts": posts,
        "commentaries": commentaries,
        "is_paginated": True,
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post


def comment_create(request:HttpRequest) -> HttpResponse:
    pk = request.POST["num-of-post"]
    comment = request.POST["comment"]
    user_id = request.POST["user-id"]

    Commentary.objects.create(content=comment, user_id=user_id, post_id=pk)
    return redirect(f"/posts/{pk}/")

def redirecttomain(request:HttpRequest) -> HttpResponse:
    return redirect("/posts/")

