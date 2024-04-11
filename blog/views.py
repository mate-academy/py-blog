from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .forms import CustomUserCreationForm, CommentForm
from blog.models import Post, User, Commentary


def index(request: HttpRequest) -> HttpResponse:

    # posts = Post.objects.all().order_by("-created_time")
    # context = {"posts": posts}
    return render(request, "blog/index.html")


class AuthorCreateView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    num_comments = Commentary.objects.count()
    template_name = "blog/post_detail.html"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_comments"] = self.num_comments
        context["form"] = CommentForm
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context


class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentForm
