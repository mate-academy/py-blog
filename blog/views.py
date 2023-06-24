from django.urls import reverse_lazy

from blog.models import Post, Commentary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_comment.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", args=[self.kwargs.get("pk")])
