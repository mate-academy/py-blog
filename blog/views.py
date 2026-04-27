from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView

from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    queryset = Post.objects.all().order_by(
        "-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments")
    template_name = "blog/post_detail.html"


class SendCommentView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.instance.post = Post.objects.get(id=pk)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail",
                       kwargs={"pk": self.kwargs.get("pk")})
