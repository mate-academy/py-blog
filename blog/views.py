from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.all()
        .select_related("owner")
        .prefetch_related("comments")
    )


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


@login_required
def create_commentary_view(
    request: HttpRequest,
    pk: int
) -> HttpResponseRedirect:
    post = Post.objects.get(pk=pk)
    form = CommentaryForm(request.POST)
    if form.is_valid():
        comment = Commentary(content=form.cleaned_data["content"])
        comment.post = post
        comment.user = request.user
        comment.save()
    return redirect("blog:post-detail", pk=pk)
