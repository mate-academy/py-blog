from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView

from blog.models import Post, Commentary
from django.conf import settings


class BlogListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["created_time"]
    paginate_by = 5

    def get_queryset(self):
        print(f"DEBUG: TEMPLATES DIRS: {settings.TEMPLATES[0]['DIRS']}")
        return super().get_queryset().prefetch_related("comments")


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by(
            "created_time")
        return context


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Commentary
    fields = "__all__"
    template_name = "blog/comment-form.html"

    def get_success_url(self):
        post_pk = self.kwargs.get("pk")
        return reverse("blog:post-detail", kwargs={"pk": post_pk})
