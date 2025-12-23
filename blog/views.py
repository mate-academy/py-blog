from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Commentary
from .forms import CommentForm, PostForm


class IndexView(generic.ListView, LoginRequiredMixin):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Commentary.objects.filter(
            post=self.get_object()
        )
        data["comments"] = comments_connected

        if self.request.user.is_authenticated:
            data["comment_form"] = CommentForm()

        return data

    def post(self, request, *args, **kwargs):
        post_object = self.get_object()
        if "edit_comment_id" in request.POST:
            comment_id = request.POST.get("edit_comment_id")
            comment = get_object_or_404(
                Commentary,
                pk=comment_id,
                user=request.user
            )
            comment.content = request.POST.get("edited_content")
            comment.save()
        elif "delete_comment_id" in request.POST:
            comment_id = request.POST.get("delete_comment_id")
            comment = get_object_or_404(
                Commentary,
                pk=comment_id,
                user=request.user
            )
            comment.delete()
        else:
            new_comment = Commentary(content=request.POST.get("content"),
                                     user=self.request.user,
                                     post=post_object)
            new_comment.save()
        return redirect("blog:post-detail", pk=post_object.pk)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_confirm_delete.html"
