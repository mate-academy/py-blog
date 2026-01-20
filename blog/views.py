from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    form = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx["form"] = CommentForm
        return ctx

    def post(self, request, **kwargs):
        pk = kwargs.get("pk")
        content = request.POST.get("content")
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content
        )
        return redirect("blog:post-detail", pk)
