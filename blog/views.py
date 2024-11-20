from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner"
                                           ).prefetch_related("comments")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


def post_detail_view(request, pk) -> HttpResponse:
    post = get_object_or_404(
        Post.objects.select_related("owner").
        prefetch_related("comments__user"),
        pk=pk
    )

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Commentary.objects.create(
                user=request.user,
                post_id=pk,
                content=content
            )

    context = {"post": post}

    return render(request, "blog/post_detail.html", context=context)
