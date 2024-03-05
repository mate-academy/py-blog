from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import CommentaryForm
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    paginate_by = 5


class UserPostListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs.get("user_pk")
        context["author_id"] = author_id
        return context

    def get_queryset(self):
        author_id = self.kwargs.get("user_pk")
        return Post.objects.select_related("owner").filter(owner=author_id)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (
        Post.objects.prefetch_related("comments__user")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")


class CommentaryListView(generic.ListView):
    model = Commentary

    def get_queryset(self):
        post_id = self.kwargs.get("pk")
        return Commentary.objects.filter(post=post_id)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        post_id = self.kwargs.get("pk")
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(pk=post_id)
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:comment-list",
            kwargs={"pk": self.object.post.pk}
        )


class CommentaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy(
            "blog:comment-list",
            kwargs={"pk": self.object.post.pk}
        )


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary

    def get_success_url(self):
        return reverse_lazy(
            "blog:comment-list",
            kwargs={"pk": self.object.post.pk}
        )
