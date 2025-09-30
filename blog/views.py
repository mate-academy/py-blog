from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts_list = Post.objects.order_by('-created_time')
    
    context = {
        'posts_list': posts_list,
    }
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return (
            Post.objects
            .annotate(num_comments=Count("comments"))
        )


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(CreateView):
    model = Commentary
    fields = ("content",)
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:post-detail")

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_pk = self.kwargs.get("pk")
        form.instance.post = Post.objects.get(pk=post_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
