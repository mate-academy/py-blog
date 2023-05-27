from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .forms import CommentaryCreateForm
from .models import Post, Commentary


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        content = request.POST.get("content")
        pk = kwargs.get("pk")
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content
        )
        return redirect("blog:post-detail", pk)
