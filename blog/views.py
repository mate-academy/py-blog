from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .models import Post, Commentary
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = (
        Post.objects
        .select_related("owner")
        .prefetch_related("comments")
    )


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to leave a comment.")
            return self.form_invalid(form)

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
