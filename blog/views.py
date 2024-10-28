from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    return render(request, "blog/index.html",
                  {"post_list": posts})


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
