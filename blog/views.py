from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(generic.CreateView, LoginRequiredMixin):
    model = Commentary
    fields = ["content"]
    template_name = "blog/add_commentary.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        form.instance.post_id = post.id
        return super().form_valid(form)
