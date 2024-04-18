from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required


from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related("commentaries")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


@login_required
def add_comment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        request
        content = request.POST.get("content")
        user = request.user
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)
        
        comment = Commentary(user=user, post=post, content=content)
        comment.save()
    else:
        pass
    return redirect(f"/posts/{post.id}")
