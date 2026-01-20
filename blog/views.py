from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    template_name = "blog/commentary_form.html"
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
