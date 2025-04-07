from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Commentary, Post


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["post_pk"]}
        )
