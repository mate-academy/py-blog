from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by("-created_time")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries__user"
    )

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        if request.user.is_authenticated:
            content = request.POST.get("content")

            if content:
                Commentary.objects.create(
                    user=request.user,
                    post=post,
                    content=content,
                )

        return redirect("blog:post-detail", pk=post.pk)
