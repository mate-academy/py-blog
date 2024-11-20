from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
