from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(IndexListView, self).get_queryset()
        queryset = (
            queryset.select_related("owner").prefetch_related("commentaries")
        )
        return queryset


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.prefetch_related("commentaries").get(pk=pk)
    context = {
        "post": post,
        "form": CommentaryCreateForm()
    }
    if request.method == "GET":
        return render(
            request,
            "blog/post_detail.html",
            context=context
        )
    if request.method == "POST":
        form = CommentaryCreateForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                Commentary.objects.create(
                    user=request.user,
                    post_id=pk,
                    content=form.cleaned_data["content"]
                )
                return HttpResponseRedirect(
                    reverse("blog:post-detail", kwargs={"pk": pk}))

            context = {"post": post, "form": form}
            return render(request, "blog/post_detail.html", context=context)

        form.errors["unauthorized"] = "You should be authorized to be able to write comments."
        context = {"post": post, "form": form}
        return render(request, "blog/post_detail.html", context=context)
