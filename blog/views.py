from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.
                select_related("owner").
                prefetch_related("comments__user")
                )


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content",)
    template_name = "includes/comment_form.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post.pk})
