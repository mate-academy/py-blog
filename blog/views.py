from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    fields = "__all__"
    context_object_name = "post_list"
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentaries")
    )
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_create.html"

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.request.GET["pk"]})

    def form_valid(self, form):
        content = form.save(commit=False)
        content.user = self.request.user
        content.post = Post.objects.get(id=self.request.GET["pk"])
        content.save()
        return super().form_valid(form)
