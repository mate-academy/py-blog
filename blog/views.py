from django.views import generic
from blog.models import Post, Commentary
from django.db.models import Count
from django.urls import reverse_lazy, reverse



class PostListView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = "-created_time"
    paginate_by = 5

    def get_queryset(self):
        return (
            Post.objects
            .select_related("owner")
            .annotate(comments_count=Count("comments"))
        )


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return (
            Post.objects
            .select_related("owner")
            .prefetch_related("comments")
        )


class CommentCreateView(LoginMixinRequierd, generic.CreateView):
    model = Commentary
    fields = ["content",]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"


    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)