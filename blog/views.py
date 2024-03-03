from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.all()
        .order_by("-created_time")
        .select_related("owner")
    )


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )
