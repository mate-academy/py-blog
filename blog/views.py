from django.views import generic
from blog.models import Post, Commentary
from django.db.models import Count
from blog.forms import CommentaryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
