from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
