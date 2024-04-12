from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .forms import CustomUserCreationForm, CommentForm
from blog.models import Post, User, Commentary


class AuthorCreateView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm


class IndexListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "post_list"
    paginate_by = 5


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(generic.DetailView):
    model = Post
    # template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get("pk")
        context["num_comments"] = Commentary.objects.filter(post_id=post_id).count()
        context["form"] = CommentForm
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        post_id = kwargs["pk"]

        if self.request.method == "POST":
            form = CommentForm(request.POST)

            if form.is_valid():
                content = form.cleaned_data["content"]
                Commentary.objects.create(
                    user=user,
                    post_id=post_id,
                    content=content
                )
                return redirect("blog:post-detail", pk=post_id)


class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentForm
