from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary

from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    paginate_by = 5


class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post-detail", pk=post.pk)
        form = CommentaryForm()
    return render(request, "includes/add_comment_to_post.html", {"form": form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Commentary, pk=pk)
    comment.delete()
    return redirect("blog:post-detail", pk=comment.post.pk)
