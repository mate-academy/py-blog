from django.urls import reverse_lazy
from django.views import generic

from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )
