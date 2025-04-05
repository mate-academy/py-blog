from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.select_related(
            "owner"
        ).prefetch_related("comments")


class PostListDetail(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_comments"] = self.object.comments.all()
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=self.object,
                content=form.cleaned_data["content"]
            )
        return redirect("blog:post-detail", pk=self.object.pk)
