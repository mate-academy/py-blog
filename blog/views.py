from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
