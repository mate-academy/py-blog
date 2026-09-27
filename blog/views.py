from typing import Any

from django.db.models.aggregates import Count
from django.http.response import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.annotate(
        comments_count=Count("commentaries")
    ).order_by(
        "-created_time"
    )


class PostDetailView(FormMixin, DetailView):
    model = Post
    queryset = (
        Post.objects.all()
        .select_related("owner")
        .prefetch_related("commentaries__user")
        .annotate(comments_count=Count("commentaries"))
    )
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_success_url(self) -> str:
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request: Any, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form: CommentaryForm) -> HttpResponse:
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
