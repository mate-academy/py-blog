from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    paginate_by = 5
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentary_set"))

