from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import User, Post


@login_required
def index(request: HttpRequest) -> HttpResponse:
    list_posts = Post.objects.all().order_by("-created_time")
    pagination = Paginator(list_posts, 5)
    context = {
        "list_posts": list_posts,
        "pagination": pagination,

    }
    return render(request,
                  "blog/index.html", context)


class PostDetailView(LoginRequiredMixin,
                     DetailView):
    model = Post
