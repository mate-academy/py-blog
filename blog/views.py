from typing import Any


from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.forms import CommentaryForm
from django.db.models import Count


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("owner")
            .annotate(comments_count=Count("comments"))
            .order_by("-created_time")
        )


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(
            user=self.request.user, post=self.get_object()
        )

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST, user=request.user, post=self.get_object()
        )
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related("comments", "comments__user")
        )
