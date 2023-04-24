from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.all().prefetch_related("owner__commentaries")


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("owner__commentaries")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("user", "post", "content", )
    template_name = "blog/commentary_form.html"
    queryset = Commentary.objects.all().prefetch_related("user__posts")
