from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from .forms import CommentForm
from .models import Post


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5

    queryset = Post.objects.select_related("owner")


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.select_related("user")
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
