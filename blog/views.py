from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.db.models import Count
# from .forms import CommentForm
from .models import *
from .models import Commentary


def index(request):
    all_posts = Post.objects.annotate(comment_count=Count('commentary'))
    posts_per_page = 5
    paginator = Paginator(all_posts, posts_per_page)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "is_paginated": paginator.num_pages > 1,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# class AddCommentView(View):
#     template_name = 'blog/add_comment.html'
#
#     def get(self, request, *args, **kwargs):
#         post_id = kwargs.get('post_id')
#         post = get_object_or_404(Post, pk=post_id)
#         comment_form = CommentForm()
#         return render(request, self.template_name,
#                       {'post': post, 'comment_form': comment_form})
#
#     def post(self, request, *args, **kwargs):
#         post_id = kwargs.get('post_id')
#         post = get_object_or_404(Post, pk=post_id)
#         comment_form = CommentForm(request.POST)
#
#         if comment_form.is_valid():
#             content = comment_form.cleaned_data['content']
#             Commentary.objects.create(user=request.user, post=post,
#                                       content=content)
#
#             return redirect('your_post_detail_url', pk=post_id)
#
#         return render(request, self.template_name,
#                       {'post': post, 'comment_form': comment_form})
