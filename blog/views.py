from django.views import generic

from blog.models import Post


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner")
