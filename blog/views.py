from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
)

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexListView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(
            self,
            request: HttpRequest,
            **kwargs: int
    ) -> HttpResponseRedirect:
        if self.request.method == "POST":
            Commentary.objects.create(
                user_id=request.user.id,
                content=request.POST["content"],
                post_id=kwargs["pk"]
            )
        return redirect("blog:post-detail", pk=kwargs["pk"])
