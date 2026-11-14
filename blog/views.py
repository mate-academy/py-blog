from django.shortcuts import render, get_object_or_404
from django.views import generic

from blog.models import Post, Commentary


def index(request):
    post_list = Post.objects.all().order_by("-created_time")[:5]
    return render(request, "blog/index.html", {"post_list": post_list})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = Commentary.objects.filter(post=self.object)
        return context
