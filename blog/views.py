from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Commentary, Post, User


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all()


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")

    def get_context_data(self, **kwargs):
        context = super(CommentaryCreateView, self).get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super(CommentaryCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.kwargs["pk"], })
