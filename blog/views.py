from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/commentary_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post.pk})
