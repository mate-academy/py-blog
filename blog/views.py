from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .form import CommentaryCreateForm

from blog.models import Post, Commentary


class BlogView(LoginRequiredMixin, generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/blog_list.html"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = CommentaryCreateForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "You must be authenticated to post a comment")
            return self.form_invalid(form)
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.kwargs.get("pk")})
