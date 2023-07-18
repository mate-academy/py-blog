from django.views import generic
from django.shortcuts import render

from blog.models import Post


def index(request):
    return render(request, "blog/index.html")


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post
