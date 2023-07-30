from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CommentaryForm
from blog.models import User, Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-created_time", ]
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        commentaries = post.commentaries.all()
        form = CommentaryForm()
        return render(request,
                      "blog/post_detail.html",
                      {
                          "post": post,
                          "commentaries": commentaries,
                          "form": form
                      })

    @staticmethod
    def post(request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        commentaries = post.commentaries.all()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
        return render(request, "blog/post_detail.html", {
            "post": post,
            "commentaries": commentaries,
            "form": form
        })


class UserListView(generic.ListView):
    model = User
    context_object_name = "user_list"
    template_name = "blog/user_list.html"
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"
