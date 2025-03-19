from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.models import User, Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    list_posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(list_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "list_posts": page_obj,
        "pagination": paginator,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
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
        return render(request, self.template_name,
                      {"post": post, "form": form})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
