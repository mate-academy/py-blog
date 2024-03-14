from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Commentary, Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs["pk"]
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})
