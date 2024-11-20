from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class PostsListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        post = self.get_object()
        user = request.user

        saved_form = form.save(commit=False)
        saved_form.post = post
        saved_form.user = user

        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)
