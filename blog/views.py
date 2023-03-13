from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form) -> HttpResponse:
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    template_name = "blog/commentary_form.html"
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")

    def form_valid(self, form) -> HttpResponse:
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(id=self.kwargs["pk"])
        comment.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
