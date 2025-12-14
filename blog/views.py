from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Commentary
from .forms import CommentaryForm


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.commentaries.order_by("-created_time")
        context["comments"] = comments
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            post = self.get_object()
            form = CommentaryForm(request.POST)
            form.add_error(None, "You must be authenticated to post comments.")
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)

        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(reverse("blog:post-detail",
                                    kwargs={"pk": post.pk}))
        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)
