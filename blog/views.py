from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect

from .forms import CommentaryForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentaries")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().prefetch_related("commentaries__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommentaryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
