from blog.models import Post, Commentary
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        form.instance.post_id = post.id
        return super().form_valid(form)
