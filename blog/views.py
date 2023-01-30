from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
        "form": CommentaryForm()
    }
    if request.method == "GET":
        return render(request, "blog/post_detail.html", context=context)

    elif request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=form.cleaned_data["content"])
        return render(request, "blog/post_detail.html", context=context)
