from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk):
    post = get_object_or_404(
        Post.objects.select_related("owner").
        prefetch_related("commentaries__user"),
        pk=pk
    )

    if request.method == "POST":
        content = request.POST.get("content")
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content
        )

    context = {"post": post}

    return render(request, "blog/post_detail.html", context=context)
