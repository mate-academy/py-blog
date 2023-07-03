from django.views import generic

from blog.models import Post


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["-created_time"]
