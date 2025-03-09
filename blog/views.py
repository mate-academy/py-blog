from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from blog import models
from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not isinstance(request.user, AnonymousUser):
            Commentary.objects.create(
                user=request.user,
                post=self.object,
                content=request.POST["text"],
            )
            return redirect("blog:post-detail", pk=self.object.pk)
        return render(request, "blog/post_detail.html", {
            "msg": "Authorization Required",
            "post": self.object,
        })
