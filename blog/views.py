from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


# Create your views here.


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/index.html'
    queryset = Post.objects.all().order_by('-created_time')


def post_detail(request: HttpRequest, pk) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    comments = post.commentaries.all()
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "form": form
    }

    return render(request, 'blog/post_detail.html', context=context)
