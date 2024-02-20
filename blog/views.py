from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        comments = post.comments.all()
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {"post": post, "comments": comments, "form": form},
        )

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        comments = post.comments.all()
        form = self.form_class(request.POST)

        if form.is_valid():
            content = form.save(commit=False)
            content.post = post
            content.author = request.user
            content.save()
            return redirect("blog:post-detail", pk=post.pk)

        return render(
            request,
            self.template_name,
            {"post": post, "comments": comments, "form": form},
        )
