from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import DetailView

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects.select_related("author")
        .prefetch_related("commentary_set")
        .order_by("-created_time")
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
    }
    return render(request, "blog/../../templates/blog/index.html", context)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("text",)


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self) -> QuerySet:
        return (
            super()
            .get_queryset()
            .select_related("author")
            .prefetch_related("commentary_set__author")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


def commentary_create(request: HttpRequest, pk: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.author = request.user
            commentary.post = post
            commentary.save()
            return redirect("blog:post-detail", pk=pk)

    return redirect("blog:post-detail", pk=pk)
