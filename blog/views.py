from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.prefetch_related("commentary")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        post_id = self.request.POST.get("post_id")
        form.instance.post = get_object_or_404(Post, pk=post_id)
        return super().form_valid(form)

    def get_success_url(self) -> HttpResponse:
        return self.object.post.get_absolute_url()


class CommentaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentary

    def get_success_url(self) -> HttpResponse:
        return self.object.post.get_absolute_url()

