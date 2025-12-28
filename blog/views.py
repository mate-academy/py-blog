from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .models import Post, Commentary
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return self.form_valid(form)

        return self.form_invalid(form)
