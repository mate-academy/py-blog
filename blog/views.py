from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all()


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    template_name = "blog/comment_create.html"
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.request.user.id)
        return super().form_valid(form)

    def get_success_url(self):
        user_id = self.object.user.id
        return reverse_lazy("blog:post-detail", args=[user_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.request.user.id)
        return context


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/post_list.html"
    queryset = Post.objects.all()
