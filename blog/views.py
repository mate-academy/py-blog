from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from blog.forms import CommentaryCreateForm
from blog.models import Commentary, Post, User


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    ordering = ["-created_time"]
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    template_name = "blog/index.html"
    paginate_by = 5


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = "user_list"
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryCreateForm()
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("backstage:post-list")
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryCreateForm()

        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("backstage:post-list")
    template_name = "blog/commentary_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_id"] = kwargs["pk"]
        return context

    def post(self, *args, **kwargs):
        print(kwargs)
        content = self.request.POST.get("content")
        pk = self.kwargs.get("pk")
        user = self.request.user
        Commentary.objects.create(user=user,
                                  post_id=pk,
                                  content=content)

        return redirect("blog:post-detail", pk)

    def get_success_url(self):

        return reverse_lazy("blog:post-detail", self.kwargs["pk"])
