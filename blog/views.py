from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    paginate_by = 5


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            "form": CommentaryForm(),
            "post": post,
        }
        return render(request, "blog/post_detail.html", context=context)
    elif request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))

        form = CommentaryForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post_id=pk,
                content=form.cleaned_data["content"]
            )
            context = {"post": post, "form": CommentaryForm()}
            return render(request, "blog/post_detail.html", context=context)
