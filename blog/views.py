from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CommentaryForm
from .models import Post, Commentary
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.all().prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs["pk"]
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})
