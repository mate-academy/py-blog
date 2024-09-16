from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    context = {
        "posts": posts,
        "page_obj": page_obj
    }

    return render(request, "blog/index.html", context=context)

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    comments = post.commentaries.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.owner = request.user
            new_comment.save()
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form
        }
    )


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "crud/post_form.html"
