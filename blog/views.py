from django.core.paginator import Paginator
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "all_posts": all_posts,
        "page_obj": page_obj
    }
    return render(
        request,
        "blog/index.html",
        context=context,
    )


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ("content",)
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/comment_form.html"
