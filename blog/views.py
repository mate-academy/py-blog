from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = (
        Post
        .objects
        .select_related("owner")
        .prefetch_related("comments")
        .order_by("-created_time")
    )

    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "post_list": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.id)

        return self.render_to_response(self.get_context_data(form=form))
