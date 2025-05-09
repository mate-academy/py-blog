from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .models import Post, Commentary, User


@login_required
def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)

    num_page = request.GET.get("page")
    page_obj = paginator.get_page(num_page)

    context = {
        "post_list": page_obj,
    }

    return render(request, "blog/index.html", context)


@login_required
def create_comment(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(id=pk)
    user = request.user
    content = request.POST.get("content")
    Commentary.objects.create(
        post=post,
        user=user,
        content=content
    )

    return redirect("blog:post-detail", pk=pk)



class PostDetailView(generic.DetailView):
    model = Post
