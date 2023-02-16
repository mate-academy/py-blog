from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostsListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Commentary.objects.filter(post_id=pk)

    if request.method == "POST":
        content = request.POST["content"]
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content,
        )

    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/post_detail.html", context=context)
