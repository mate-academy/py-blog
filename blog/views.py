from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


def index_view(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    context = {"post_list": posts}
    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


@require_POST
def comment_view(request: HttpRequest, post_id) -> HttpResponse:
    post = get_object_or_404(
        Post,
        id=post_id
    )
    comment = None
    form = CommentaryForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

    context = {
        "form": form,
        "post": post,
        "comment": comment,
    }

    return render(request, "blog/comment.html", context=context)
