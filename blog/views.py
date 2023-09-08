from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


def index(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5)

    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    context = {
        "post_list": post_list
    }

    return render(
        request,
        template_name="blog/index.html",
        context=context,
    )


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/comment_form.html"
