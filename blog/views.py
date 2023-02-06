from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time").select_related("owner").prefetch_related("commentaries")
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related("commentaries__user")
    template_name = "blog/post_detail.html"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:post-detail")
