from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from .models import Post, Commentary
from .forms import CommentaryForm


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be authenticated to comment.")
            return self.render_to_response(self.get_context_data(form=form))

        if request.user.is_authenticated and form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)
