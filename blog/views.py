from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from blog.form import CommentaryCreateForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comment")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreateForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        content = request.POST.get("content")
        pk = kwargs.get("pk")
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content
        )
        return redirect("blog:post-detail", pk)
