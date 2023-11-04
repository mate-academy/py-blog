from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post


@login_required()
def add_new_comment(request: HttpRequest, pk: int) -> HttpResponse:
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    commentary_content = request.POST.get("new_comment")
    Commentary.objects.create(
        user=user,
        post=post,
        content=commentary_content
    )
    return redirect("blog:post-detail", pk=post.id)
