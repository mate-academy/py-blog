from django.shortcuts import render
from django.views import generic
from blog.models import Post, Commentary, User


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = Commentary.objects.filter(post_id=pk)

    if request.method == "POST":
        content = request.POST["content"]
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content,
        )

    context = {
        "post": post,
        "comment_list": comment_list,
    }

    return render(request, "blog/post_detail.html", context=context)
