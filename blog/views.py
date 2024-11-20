from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = (
            Post.objects.order_by("-created_time").select_related("owner")
        )
        return queryset


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["form"] = CommentForm()
        return data


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
    return redirect("blog:post-detail", pk=post.pk)
