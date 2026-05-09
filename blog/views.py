from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class PostList(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentaryForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user
        comment.save()
        return redirect("blog:post-detail", pk=self.object.pk)
