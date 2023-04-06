from blog.forms import CommentaryForm
from blog.models import Post, Commentary
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommentaryForm
    model = Commentary
    fields = "content"
    success_url = reverse_lazy("blog:post-detail")
