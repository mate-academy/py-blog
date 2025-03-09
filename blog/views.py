from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Commentary
from .forms import CommentaryForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Related comments for the post
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentaryForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })
