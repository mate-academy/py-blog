from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


@login_required
def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.created_time = timezone.now()
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentaryForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
