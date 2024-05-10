from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentForm, PostForm
from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post_object = self.get_object()
        new_comment = Commentary(
            content=request.POST.get("content"),
            user=self.request.user,
            post=post_object,
        )
        new_comment.save()
        return redirect("blog:post-detail", pk=post_object.pk)


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/form.html"
    form_class = PostForm


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/form.html"
    success_url = reverse_lazy("blog:index")
    form_class = PostForm


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/confirmation.html"
    success_url = reverse_lazy("blog:index")
    form_class = PostForm


def edit_comment(request, pk):
    comment = get_object_or_404(Commentary, pk=pk, user=request.user)
    comment.content = request.POST.get("edited_content")
    comment.save()
    return redirect("blog:post-detail", pk=comment.post.pk)


def delete_comment(request, pk):
    comment = get_object_or_404(Commentary, pk=pk, user=request.user)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("blog:post-detail", pk=post_pk)
