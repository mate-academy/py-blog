from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import redirect

from .models import Post, Commentary
from .forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return redirect("blog:post-detail", pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs=self.kwargs)
