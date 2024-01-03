from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Post
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(initial={"id": self.object})
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.user = self.request.user
        form.save()
        return super(PostDetailView, self).form_valid(form)
