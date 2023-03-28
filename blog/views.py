from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView


from blog.models import Post, Commentary


@login_required
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

class CommentCreateView(CreateView):
    model = Commentary
    fields = "__all__"
    # fields = ['content']
    context_object_name = 'comment'
    template_name = 'blog/comment_form.html'

    success_url = reverse_lazy("blog:index")



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    template_data = {

    }
    context_object_name = 'post'
    success_url = reverse_lazy("blog:index")
