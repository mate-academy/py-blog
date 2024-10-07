from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "commentaries": Commentary.objects.select_related(),
        "users": get_user_model(),
        "post_list": page_obj.object_list,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView, generic.CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.post = self.get_object()
        commentary.user = self.request.user
        commentary.save()
        return super().form_valid(form)
