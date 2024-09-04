from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = {
            "post": post,
            "comments": post.comments.all(),
            "number_of_comments": post.comments.all().count(),
            "comment_form": CommentForm(),
        }
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        else:
            context = self.get_context_data()
            context["comment_form"] = form
            return self.render_to_response(context)


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    template_name = "blog/comment_delete_confirm.html"

    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy("blog:post-detail", kwargs={"pk": comment.post_id})
