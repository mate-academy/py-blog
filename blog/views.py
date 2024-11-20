from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("comments__user")
    success_url = reverse_lazy("blog:post-detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, **kwargs):
        content = request.POST["content"]
        user = request.user
        post_id = kwargs["pk"]
        comment = Commentary(content=content, user=user, post_id=post_id)
        comment.save()
        return HttpResponseRedirect(
            reverse_lazy("blog:post-detail", args=[post_id])
        )
