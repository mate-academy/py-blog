from django.views import generic

from blog.models import User, Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

