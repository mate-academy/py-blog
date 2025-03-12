from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Commentary


# def index(request: HttpRequest) -> HttpResponse:
#     post_list = Post.objects.all().order_by("-created_time")
#     context = {
#         "post_list": post_list,
#     }
#     return render(request, "blog/index.html", context)

class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()  # Получаем текущий пост
        context['comments'] = post.comments.all()  # Получаем комментарии для этого поста
        return context
class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ("content",)
    template_name = "blog/comment_create.html"
    success_url = "blog:post_detail"
