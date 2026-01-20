from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("comments")
    ordering = ["created_time"]
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "comments", "comments__user"
    ).select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect(
                reverse(
                    "blog:post-detail", kwargs={"pk": self.object.pk}
                )
            )

        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)
