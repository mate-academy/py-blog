from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.core.paginator import Paginator

from blog.forms import CommentaryForm
from blog.models import Post, Commentary, User


def index(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, per_page=5)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_pages": paginator.num_pages
    }

    return render(request, "blog/index.html", context=context)


def post_detail_view(request, pk: int):
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
