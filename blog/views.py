from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Commentary


def index(request):
    posts_list = Post.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(posts_list, 5)

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/comment_create.html"
