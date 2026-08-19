from django.core.paginator import Paginator
from django.db.models import Count, Prefetch
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects
        .select_related("owner")
        .annotate(comment_count=Count("commentaries"))
        .order_by("-created_time")
    )

    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "blog/index.html",
        context={
            "posts": page_obj,
            "post_list": page_obj,
            "page_obj": page_obj,
            "is_paginated": page_obj.has_other_pages(),
        }
    )


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (
        Post.objects
        .select_related("owner")
        .annotate(comment_count=Count("commentaries"))
        .prefetch_related(
            Prefetch(
                "commentaries",
                queryset=Commentary.objects.select_related("user"),
            )
        )
    )
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = kwargs.get(
            "comment_form",
            CommentaryForm(),
        )
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()

        if not request.user.is_authenticated:
            login_url = reverse("login")
            return redirect(f"{login_url}?next={request.path}")

        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)
