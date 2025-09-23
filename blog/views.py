from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().select_related("owner")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk})
        )
