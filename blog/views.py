from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentaryForm
from .models import Post, Commentary
import datetime


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("post_comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        new_comment = Commentary(
            user=request.user,
            post=post,
            created_time=datetime.datetime.now(),
            content=request.POST.get("content")
        )
        new_comment.save()
        return redirect(reverse_lazy('blog:post-detail', args=[post.pk]))
