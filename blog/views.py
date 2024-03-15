from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.db.models import Count, Max
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.forms import CommentForm
from blog.models import Post, Commentary
from blog.services import user_services, post_services


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:dashboard")


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts_with_counts = Post.objects.annotate(
            comment_count=Count("comments"),
            latest_comment_time=Max("comments__created_time"),
        )
        most_commented = posts_with_counts.order_by("-comment_count").first()
        context["most_commented"] = most_commented
        context["publication_dates"] = post_services.get_publication_dates()
        context["authors"] = user_services.get_authors_with_post_counts()
        if self.request.GET:
            context["title"] = "Filtered Blog Posts"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get("year")
        month = self.request.GET.get("month")
        author = self.request.GET.get("author")
        if year and month:
            queryset = queryset.filter(
                created_time__year=year, created_time__month=month
            )
        if author:
            queryset = queryset.filter(owner=author)
        return queryset


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(
            Post.objects.select_related("owner"),
            pk=post_id
        )
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )


class CommentaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentary

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )


class CommentaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Commentary
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )


class DashboardListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/dashboard.html"

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Getting the user's last comment on their own post
        last_comment = (
            Commentary.objects.filter(user=self.request.user)
            .order_by("-created_time")
            .first()
        )

        # Getting the total number of posts for the current month
        current_month_posts = (
            self.get_queryset()
            .filter(created_time__month=datetime.now().month)
            .count()
        )

        context["last_comment"] = last_comment
        context["current_month_posts"] = current_month_posts
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
