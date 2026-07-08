from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by("-created_time")
    num_visits = request.session.get("num_visits", 0)
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    num_visits += 1
    request.session["num_visits"] = num_visits
    context = {
        "all_posts": all_posts,
        "num_visits": num_visits,
        "post_list": page,
    }

    return render(request, "blog/index.html", context=context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect("blog:post-detail", pk=post.pk)
        else:
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = CommentaryForm()

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "form": form,
    })
