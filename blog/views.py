from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, ListView

from .forms import CommentaryForm
from .models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by(
            "-created_time")
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect("blog:post-detail", pk=self.object.pk)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
