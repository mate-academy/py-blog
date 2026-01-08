from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        context["comments"] = (
            self.object.comments.all()
            .order_by("-created_time")
        )
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def form_valid(self, form):
        post_id = self.kwargs.get("pk")
        post_instance = get_object_or_404(Post, pk=post_id)
        form.instance.user = self.request.user
        form.instance.post = post_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs.get("pk")}
        )
