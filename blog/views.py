from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            context = self.get_context_data(form=form)
            context["error"] = "You must be logged in to submit a comment."
            return render(request, "blog/post_detail.html", context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.id)
        context = {"form": form}
        return render(request, "blog/post_detail.html", context)
