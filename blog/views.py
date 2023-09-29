from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


def post_detail(request, pk: int) -> HttpResponse:
    context = {"post": Post.objects.get(id=pk)}
    if request.method == "GET":
        return render(request, "blog/post_detail.html", context=context)
    elif request.method == "POST":
        if request.POST["content"]:
            Commentary.objects.create(
                user_id=request.POST["user_id"],
                post_id=request.POST["post_id"],
                content=request.POST["content"],
            )
        return render(request, "blog/post_detail.html", context=context)
