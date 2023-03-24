from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator

from blog.models import Post, Commentary


@login_required()
def index(request):
    post_list = Post.objects.select_related("owner").all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": paginator.get_page(page_number),
        "page_obj": page_obj
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
