from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").order_by("-created_time")

    def get_template_names(self):
        return ["blog/index.html"]


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
