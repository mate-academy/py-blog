from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]

        return super().form_valid(form)
