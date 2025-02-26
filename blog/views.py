from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.prefetch_related(
        "comments"
    ).select_related(
        "owner"
    )
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("comments__user")
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", args=(str(self.object.pk)))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to add a comment.")
            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)
