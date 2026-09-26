from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = "-created_time"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "You must be logged in to comment.")
            return self.form_invalid(form)

        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(
            Post, pk=self.kwargs["pk"]
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.object.post_id},
        )
