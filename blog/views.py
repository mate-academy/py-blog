from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Post, Commentary


@login_required
def index(request):
    """View function for the home page of the site."""

    num_users = User.objects.count()
    num_posts = Post.objects.count()
    num_commentaries = Commentary.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_posts": num_posts,
        "num_commentaries": num_commentaries,
        "num_visits": num_visits + 1,
    }

    return render(request, "blog/index.html", context=context)


class CommentaryListView(LoginRequiredMixin, generic.ListView):
    model = Commentary
    context_object_name = "commentary_list"
    template_name = "blog/commentary_list.html"
    ordering = ["-created_time"]
    paginate_by = 5


class CommentaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Commentary
    template_name = "blog/commentary_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:commentary-list")
    template_name = "blog/commentary_form.html"


class CommentaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:commentary-list")
    template_name = "blog/commentary_form.html"


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:commentary-list")
    template_name = "blog/commentary_confirm_delete.html"


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    ordering = ["created_time"]
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_form.html"


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_form.html"


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_confirm_delete.html"


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.all().prefetch_related("posts__commentaries")
