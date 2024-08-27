from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    posts = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all().prefetch_related("comments")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = []
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = Post.objects.get(pk=self.kwargs["pk"]).id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.object.post.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.kwargs["pk"])
        return context
