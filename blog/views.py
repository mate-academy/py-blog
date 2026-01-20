from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.form import CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentFormView(LoginRequiredMixin, generic.FormView):
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        comment = form.save(commit=False)
        comment.post = post
        comment.user = self.request.user
        comment.save()
        return redirect("blog:post-detail", pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        context["post"] = post
        return context
