from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Post, Commentary


def index(request):
    posts_list = Post.objects.select_related("owner").all()
    page = request.GET.get("page", 1)
    paginator = Paginator(posts_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "post_list": posts
    }

    return render(request, "blog/index.html", context=context)


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/create_update_post.html"


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/create_update_post.html"


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/confirm_delete.html"
    success_url = reverse_lazy("blog:index")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/create_update_commentary.html"
