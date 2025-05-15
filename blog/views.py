from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import CommentaryForm
from .models import Post


def index(request):
    posts_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts_list, 5)

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "index.html", {"posts": posts})


class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.order_by("-created_time")
    form = CommentaryForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.user = request.user
                new_comment.save()
        else:
            form.add_error(None, "You must be logged in to comment.")

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        }
    )
