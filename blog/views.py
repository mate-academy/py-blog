from django.shortcuts import redirect
from django.views import generic
from blog.models import Post, Commentary


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    queryset = Post.objects.all().order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        post = self.get_object()

        content = request.POST.get("content")
        if content:
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=content,
            )
        return redirect("blog:post-detail", pk=post.pk)
