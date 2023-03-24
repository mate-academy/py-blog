from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import CommentaryForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentaries")
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentaries__user")
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class AddCommentView(LoginRequiredMixin, generic.View):
    def post(self, request, pk: int) -> HttpResponse:
        post = get_object_or_404(Post, pk=pk)
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(reverse_lazy("blog:post-detail", args=[post.pk]))

        return render(
            request,
            "blog/post_detail.html",
            {"post": post, "form": form}
        )
