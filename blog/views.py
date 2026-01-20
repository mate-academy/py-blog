from blog.models import Post, Commentary
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


def post_detail_and_create(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST" and request.user.is_authenticated:
        Commentary.objects.create(
            user_id=request.user.id,
            post=post,
            content=request.POST.get("comment")
        )

        context = {
            "post": post,
            "commentaries": post.commentaries.all(),
        }

        return render(request, "blog/post_detail.html", context=context)
    elif request.method == "POST":
        return render(request, "registration/login.html")
    context = {
        "post": post,
        "commentaries": post.commentaries.all(),
    }
    return render(request, "blog/post_detail.html", context=context)
