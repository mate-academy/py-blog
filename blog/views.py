from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    paginate_by = 5


@method_decorator(login_required, name="post")
class PostDetailView(generic.DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        Commentary.objects.create(
            user=request.user,
            post=Post.objects.get(pk=kwargs["pk"]),
            content=request.POST["content"],
        )
        return HttpResponseRedirect(
            reverse("blog:post-detail", kwargs={"pk": kwargs["pk"]})
        )
