from django.urls import reverse, reverse_lazy

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments__user")


def add_comment(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        user = request.user
        content = request.POST["content"]
        Commentary.objects.create(
            user=user,
            post=post,
            content=content
        )
    return HttpResponseRedirect(
        reverse_lazy("blog:post-detail", kwargs={"pk": pk})
    )
