from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"
    template_name = "blog/index.html"

    def get_queryset(self):
        return (Post.objects.select_related(
            "owner").annotate(
            num_comments=Count("comments")).order_by(
            "-created_time"))


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )
