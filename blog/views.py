from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count("commentaries"))


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post.pk})
