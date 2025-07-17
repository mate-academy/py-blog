from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    ordering = ['-created_time']
    paginate_by = 5


class PostDetailView(
    generic.DetailView,
    LoginRequiredMixin
):
    model = Post
    template_name = 'blog/post_detail.html'
