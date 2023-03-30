from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from blog.forms import CommentForm
from blog.models import Post, Commentary, User


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    queryset = Post.objects.prefetch_related("commentary_set")


class CommentsCreateView(CreateView):
    template_name = "blog/post_detail.html"
    model = Commentary
    form_class = CommentForm
    success_url = reverse_lazy("post-detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.prefetch_related(
            "commentary_set__user"
        ).get(pk=self.kwargs["pk"])
        return context

    def post(self, request, *args, **kwargs):
        user_id = request.POST["user_id"]
        post_id = request.POST["post_id"]
        content = request.POST["content"]

        new_comment = Commentary(
            user_id=user_id,
            post_id=post_id,
            content=content
        )
        new_comment.save()

        return HttpResponseRedirect(self.request.path_info)


class LoginCreateView(CreateView):
    pass
