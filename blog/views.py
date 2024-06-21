from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = (Post.objects.select_related("owner").
             prefetch_related("commentaries__user").order_by("-created_time"))
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "blog/index.html",
        {
            "page_obj": page_obj,
        }
    )


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner").
                prefetch_related("commentaries__user"))


class CommentCreateView(generic.CreateView):
    model = Commentary
    fields = ["content",]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"
