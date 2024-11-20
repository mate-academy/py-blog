from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

# from blog.forms import CommentForm
from blog.models import Post, Commentary, User


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.id}
        )
