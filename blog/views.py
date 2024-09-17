from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms
from django.views.generic.edit import FormMixin

from blog.models import Post
from .forms import CommentForm

from .models import Commentary


class PostListView(generic.ListView):
    model = Post
    fields = "__all__"
    template_name = "blog/index.html"
    success_url = reverse_lazy("blog:post-list")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentaries.select_related("user")
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.instance.post = self.object
            form.instance.user = request.user
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)
