from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Post
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = (Post.objects.
                select_related("owner").
                prefetch_related("commentaries"))


def post_detail_plus_create_comment(
        request: HttpRequest,
        pk: int
) -> HttpResponse:
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post_id = pk
                comment.save()
                return HttpResponseRedirect(reverse(
                    "blog:post-detail",
                    kwargs={"pk": pk}
                ))
        else:
            form.errors["user"] = "You are not registered in the system."
    else:
        form = CommentaryForm()

    post = Post.objects.prefetch_related("commentaries").get(pk=pk)
    context = {
        "post": post,
        "form": form
    }
    return render(request, "blog/post_detail.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")
