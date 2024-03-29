from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Commentary.objects.filter(post=self.get_object())
        data["comments"] = comments_connected

        if self.request.user.is_authenticated:
            data["comment_form"] = CommentForm()

        return data

    def post(self, request, *args, **kwargs):
        post_object = self.get_object()
        if "edit_comment_id" in request.POST:
            comment_id = request.POST.get("edit_comment_id")
            comment = get_object_or_404(Commentary, pk=comment_id,
                                        user=request.user)
            comment.content = request.POST.get("edited_content")
            comment.save()
        elif "delete_comment_id" in request.POST:
            comment_id = request.POST.get("delete_comment_id")
            comment = get_object_or_404(Commentary, pk=comment_id,
                                        user=request.user)
            comment.delete()
        else:
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
