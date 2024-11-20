from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.order_by("created_time").select_related("owner")


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryListView(generic.ListView):
    model = Commentary


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/commentary_form.html"
