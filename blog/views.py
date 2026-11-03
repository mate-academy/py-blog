from django.contrib.auth.decorators import login_required

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    context_object_name = "post_list"
    template_name = "index.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


@login_required
def commentary_create(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    return redirect("blog:post-detail", pk=post.pk)
