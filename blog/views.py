from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDict
from django.views import generic
from django.views.generic import CreateView

from blog.forms import CommentForm, CustomUserCreationForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page = request.GET.get("page", 1)
    page_obj = paginator.get_page(page)

    print(
        f"page: {page}, "
        f"paginator.num_pages: {paginator.num_pages}, "
        f"page_obj.object_list: {len(page_obj.object_list)}"
    )

    context = {
        "post_list": page_obj.object_list,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
        "page_obj": page_obj,
    }

    return render(
        request,
        "blog/index_.html",
        context=context
    )


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        return self.render_to_response({"form": form})


class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:index")
