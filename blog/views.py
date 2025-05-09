from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post


@login_required
def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": post_list,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))
