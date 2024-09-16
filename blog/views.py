from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import CommentaryForm
from .models import Post


def index(request: HttpRequest) -> HttpResponse:
    queryset = Post.objects.all().annotate(comment_count=Count("comments"))
    paginator = Paginator(queryset, 5)

    page_num = request.GET.get("page", default=1)
    post_list = paginator.get_page(page_num)
    post_list.adjusted_elided_pages = paginator.get_elided_page_range(
        page_num, on_each_side=3, on_ends=0
    )

    context = {
        "is_paginated": True,
        "post_list": post_list,
    }
    return render(
        request=request,
        template_name="blog/index.html",
        context=context
    )


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = self.form_class()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        commentary_form = self.form_class(request.POST or None)
        if commentary_form.is_valid():
            comment = commentary_form.save(commit=False)
            comment.user = request.user
            comment.post_id = kwargs["pk"]
            comment.save()
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs=kwargs)
            )
