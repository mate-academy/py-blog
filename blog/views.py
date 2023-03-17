from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "index"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str: any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["post"] = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return context
