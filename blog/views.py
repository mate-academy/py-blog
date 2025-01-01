from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Commentary, Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.prefetch_related("comments").all()
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    context_object_name = "post"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        context = super().get_context_data(**kwargs)
        context["comments"] = Commentary.objects.filter(
            post=self.object).order_by(
            "-created_time"
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if not request.user.is_authenticated:
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    auth_error="You must be logged in to post a comment"
                )
            )

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))
