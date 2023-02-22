from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk):
    post = get_object_or_404(
        Post.objects.select_related("owner").
        prefetch_related("post_comments"),
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
