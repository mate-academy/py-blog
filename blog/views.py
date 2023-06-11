from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Commentary, Post


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5

    queryset = Post.objects.select_related("owner")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.select_related("user")
    form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    if request.user.is_authenticated:
        context["logged_in"] = True

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                **form.cleaned_data,
                post=post,
                user=request.user,
            )
        else:
            context["error"] = (
                "Invalid form"
            )

    return render(request, "blog/post_detail.html", context=context)
