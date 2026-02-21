from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import FormCommentary
from blog.models import User, Post, Commentary


def index(request):
    users_count = User.objects.count()
    posts_count = Post.objects.count()
    commentaries_count = Commentary.objects.count()

    context = {
        "users": users_count,
        "posts": posts_count,
        "commentaries": commentaries_count
    }

    return render(request, "blog/index.html", context=context)


class PostsView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"
    queryset = Post.objects.prefetch_related("post_commentaries")
    template_name = "blog/index.html"
    ordering = ["-created_time"]

class PostsDetailView(DetailView):
    model = Post


class PostsCreateComment(LoginRequiredMixin, CreateView):
    model = Commentary
    form_class = FormCommentary
    template_name = "blog/comments_create.html"
    success_url = reverse_lazy("blog:index")
