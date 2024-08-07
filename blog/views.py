from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("comments"))


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("comments__user"))

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def get_context_data(self, **kwargs) -> dict:
        context = super(CommentaryCreateView, self).get_context_data(**kwargs)
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        context["post"] = post
        context["user"] = self.request.user
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            post_id = self.kwargs.get("post_id")
            post = get_object_or_404(Post, pk=post_id)
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post_id)
