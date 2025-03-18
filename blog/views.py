from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from blog.models import Post, Commentary


@login_required
def index(request):
    posts = Post.objects.all().order_by("-created_time")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:index")


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_detail.html"
