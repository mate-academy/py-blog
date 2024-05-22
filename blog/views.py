from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from blog.models import Post, Commentary
from django.views import generic


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time").select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryListView(generic.ListView):
    model = Commentary
    template_name = "blog/post_detail.html"
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content", ]
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )
