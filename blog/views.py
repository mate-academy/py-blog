from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, User, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "templates/blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    # template_name = "templates/blog/commentary_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return context

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["post_pk"]}
        )
