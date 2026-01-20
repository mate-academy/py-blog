from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ("-created_time",)
    context_object_name = "post_list"
    template_name = "blog/post_list.html"


class CommentView(generic.DetailView):
    model = Commentary
    context_object_name = "comment"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment.all()
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(
            self.get_context_data(comment_form=form
                                  ))
