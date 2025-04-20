from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (Post.objects.select_related("owner").
                prefetch_related("commentaries").order_by("-created_time"))
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner").
                prefetch_related("commentaries__user"))


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
