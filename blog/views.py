from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Post, Commentary, User

@login_required
def index(request):
    """View function for the home page of the site."""
    num_users = User.objects.count()
    num_posts = Post.objects.count()
    num_comments = Commentary.objects.count()
    time_posts = Post.objects.order_by('-created_time')

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_posts": num_posts,
        "num_comments": num_comments,
        "num_visits": num_visits + 1,
        "time_posts": time_posts,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding comments to the context
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5
    queryset = Post.objects.all().select_related("owner")


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
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_confirm_delete.html"


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.all().prefetch_related("posts__comments")


class CommentaryListView(LoginRequiredMixin, generic.ListView):
    model = Commentary
    context_object_name = "commentary_list"  # Замінили на відповідну змінну
    template_name = "blog/commentary_list.html"  # Замінили шаблон на відповідний для коментарів
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["post", "user", "content"]  # Вказуємо конкретні поля, які потрібно заповнити
    success_url = reverse_lazy("blog:comment-list")  # Замінили на правильний шлях
    template_name = "blog/commentary_form.html"  # Замінили шаблон на відповідний для створення коментаря


class CommentaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:comment-list")
    template_name = "blog/commentary_form.html"


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    success_url = reverse_lazy("blog:comment-list")
    template_name = "blog/commentary_confirm_delete.html"

