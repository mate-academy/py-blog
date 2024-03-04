from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import CommentForm
from .models import Post, Commentary


def index(request):
    posts = Post.objects.all().order_by("-created_time")
    page = request.GET.get("page", 1)
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"post_list": posts}
    return render(request, "index_list.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


class CreateCommentView(generic.CreateView):
    template_name = "post_detail.html"

    def get(self, request, pk) -> HttpResponse:
        post = get_object_or_404(Post, pk=pk)
        return render(
            request, "post_detail.html", {"post": post, "form": CommentForm()}
        )

    def post(self , request , pk) -> HttpResponse:
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=pk)
            date = request.POST.get("created_time")
            content = request.POST.get("content")
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=content,
                created_time=date
            )

        else:
            post = get_object_or_404(Post, pk=pk)
            form = CommentForm()
            error_context = {
                "post": post,
                "form": form,
                "error": "You must be logged in to add a comment.",
            }
        return render(request, "post_detail.html", error_context)
