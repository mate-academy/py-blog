from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Commentary



class PostDetailView(generic.DetailView):
    model = Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    context_object_name = "post_list"


@login_required
def add_comment(request, pk):
    if request.method == "POST":
        comment_content = request.POST.get("comment")
        if comment_content:
            post = Post.objects.get(id=pk)
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=comment_content
            )
            messages.success(request, "Comment successfully added!")
        else:
            messages.warning(request, "A comment cannot be empty!")
    return redirect("blog:post-detail", pk=pk)
