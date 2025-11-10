from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView


from .models import Post, Commentary
from .forms import CommentaryForm


def index(request):
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = (
            self.object.commentaries.all().order_by("-created_time")
        )
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return self.get(request, *args, **kwargs)

        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Commentary

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )
