from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models.aggregates import Count
from django.views import generic

from blog.models import Post



class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").annotate(com_num=Count("comments"))
    template_name = "base.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post