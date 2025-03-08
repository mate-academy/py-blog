from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailtView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog:post_detail")
    post_template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        Commentary.objects.create(
            user=self.object.owner,
            post=self.object,
            content=request.POST["text"],
        )
        return redirect("blog:post-detail", pk=self.object.pk)
