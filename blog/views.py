from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


# Create your views here LoginRequiredMixin.
class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by(
        "-created_time"
    ).prefetch_related("commentaries")

    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")


class CommentaryListView(generic.ListView):
    model = Commentary
    template_name = "blog/post_detail.html"

    context_object_name = "commentaries"

    def get_queryset(self):
        post_id = self.kwargs.get("pk")
        post = Post.objects.get(pk=post_id)
        commentaries = Commentary.objects.filter(
            post=post
        ).prefetch_related("user")

        return commentaries

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs["pk"]
        post = Post.objects.get(pk=post_pk)
        context["post"] = post

        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail")
