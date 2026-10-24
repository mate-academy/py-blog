from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.form import CommentForm
from blog.models import Post, Commentary


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
        "is_paginated": page_obj.has_other_pages()
    }
    return render(request, "index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content",)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
