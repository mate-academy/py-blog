from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView

from .forms import CommentForm
from .models import Post, Commentary


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").annotate(
        comments_count=Count("comments")
    )


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            form = CommentForm(request.POST)
            form.add_error(
                "content",
                "Only registered users can leave comments."
            )
            return self.render_to_response(self.get_context_data(form=form))

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect(
                reverse(
                    "blog:post-detail",
                    kwargs={"pk": self.object.pk}
                )
            )

        return self.render_to_response(self.get_context_data(form=form))
