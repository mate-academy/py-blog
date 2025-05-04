from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryModelForm
from blog.models import Post


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects
        .annotate(comment_count=Count("commentaries"))
        .order_by("-created_time")
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryModelForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryModelForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
