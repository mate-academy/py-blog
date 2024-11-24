from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time").select_related("owner")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(generic.View):
    @staticmethod
    def post(request, pk):
        if request.user.is_anonymous:
            context = {
                "post": get_object_or_404(Post, id=pk),
                "errors": "Only for authorized users",
            }
            return render(request, "blog/post_detail.html", context)
        else:
            if request.method == "POST":
                post = get_object_or_404(Post, id=pk)
                user = request.user
                data = request.POST
                commentary = data.get("commentary")
                if not commentary:
                    context = {
                        "post": get_object_or_404(Post, id=pk),
                        "errors": "Write smth",
                    }
                    return render(request, "blog/post_detail.html", context)
                Commentary.objects.create(
                    content=commentary,
                    post=post,
                    user=user,
                )
            return render(
                request,
                "blog/post_detail.html",
                {"post": get_object_or_404(Post, id=pk)},
            )
