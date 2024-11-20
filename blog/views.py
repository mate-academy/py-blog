from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    posts = Post.objects.select_related("owner").prefetch_related("comments")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    context = {
        "post_list": post_list,
        "is_paginated": True,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "comments__user",
        "comments"
    )
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(self.request.POST or None)
        return context

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return self.form_valid(form=form)
        return self.form_invalid(form=form)
