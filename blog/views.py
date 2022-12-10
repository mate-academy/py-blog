from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    paginate_by = 5

