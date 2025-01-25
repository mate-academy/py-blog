from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commentary, Post
from .forms import CommentaryForm


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner").prefetch_related("comments")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    queryset = Post.objects.select_related("owner").prefetch_related("comments")

    def get_context_data(self, **kwargs):
        """Add comment form to context"""
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        """Ensure the post object is available in the template"""
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, id=self.kwargs["pk"])  # Pass the post
        return context

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect back to the post detail page after submitting"""
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
