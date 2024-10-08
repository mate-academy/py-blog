from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentCreateView(generic.View):
    @method_decorator(login_required)
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comment = request.POST.get("comment")

        if comment:
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=comment,
            )
        return redirect("blog:post-detail", pk=post_id)
