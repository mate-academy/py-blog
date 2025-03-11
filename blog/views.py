from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView

from .models import Post


def index(request):
    posts_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"