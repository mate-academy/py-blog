from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    comments = Commentary.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    return render(
        request,
        "index.html",
        {
            "page_obj": page_obj,
            "is_paginated": page_obj.has_other_pages(),
            "post_list": page_obj,
            "comments": comments,
        },
    )


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    fields = "__all__"
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return self.form_valid(form)
        return self.form_invalid(form)
