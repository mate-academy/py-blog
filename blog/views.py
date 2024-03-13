from django.db.models import Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post = Post.objects.order_by("-created_time")
    commentary_count = Post.objects.annotate(num_comments=Count("commentary"))
    context = {
        "posts": post,
        "post_count": commentary_count,
    }

    return render(request, "blog/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post
