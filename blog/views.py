from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    success_url = reverse_lazy("blog:post-list")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("commentaries")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", args=[self.kwargs.get("pk")])
