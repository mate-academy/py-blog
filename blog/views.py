from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    get_context_name = "post_list"
    queryset = Post.objects.all().order_by("owner")


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryCreateForm()
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
