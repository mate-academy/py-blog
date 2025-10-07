from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.models import Post, Commentary
from blog.forms import CommentForm


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comments.all().order_by(
            "created_time")
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to add a comment.")
            messages.error(request, "Увійдіть, щоб додати коментар.")
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Коментар успішно додано!")
            return redirect("blog:post-detail", pk=post.pk)
        else:
            messages.error(request, "Будь ласка, виправте помилки у формі.")
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)
