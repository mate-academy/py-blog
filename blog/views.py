from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        content = request.POST.get("content")
        user = request.user
        post_id = request.POST.get("post")
        post = Post.objects.get(pk=post_id)

        comment = Commentary(user=user, post=post, content=content)
        comment.save()
        return redirect(f"/posts/{post.id}/")
