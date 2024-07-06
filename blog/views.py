from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post, Commentary
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["form"] = CommentForm()
        return data


@login_required
def commentary_create_view(
    request: HttpRequest, pk: int
) -> HttpResponseRedirect:
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                post_id=pk, user=request.user, **form.cleaned_data
            )
    return HttpResponseRedirect(reverse("blog:post-detail", args=(pk,)))
