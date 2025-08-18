from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj.object_list,
        "page_number": page_number,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    }

    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            if not request.user.is_authenticated:
                form.add_error(None, "You must be logged in to comment")
                return self.form_invalid(form)

            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.created_time = timezone.now()
            commentary.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs) -> dict:
        data = super().get_context_data(**kwargs)
        data["form"] = self.get_form()
        return data
