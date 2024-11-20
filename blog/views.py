from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Post, Commentary
from .forms import CommentForm


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            content = request.POST["content"]
            user = request.user
            post_id = kwargs["pk"]
            comment = Commentary(content=content, user=user, post_id=post_id)
            comment.save()
            return redirect(request.META["HTTP_REFERER"])
        return redirect("login")
