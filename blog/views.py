from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CreateCommentForm
from blog.models import Post, Commentary, User


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.select_related(
            "owner"
        ).prefetch_related(
            "comments"
        ).order_by("-created_time")


class PostDetailedView(generic.DetailView):
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    model = Post

    def get_queryset(self):
        return Post.objects.prefetch_related(
            Prefetch(
                "comments",
                queryset=Commentary.objects.select_related("user"))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_form"] = CreateCommentForm()
        return context


class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
