from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView

from .models import Post, Commentary, CommentForm


def index(request):
    posts = Post.objects.annotate(
        comment_count=Count("commentaries")).order_by(
        "-created_time"
    )

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")

    posts = paginator.get_page(page)
    is_paginated = posts.has_other_pages()

    context = {
        "post_list": posts,
        "is_paginated": is_paginated,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView, generic.FormView):
    model = Post
    queryset = Post.objects.annotate(comment_count=Count("commentaries"))
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = sorted(
            post.commentaries.all(),
            key=lambda c: c.created_time,
            reverse=True
        )
        context["sorted_comments"] = comments
        return context

    def form_valid(self, form):
        post = self.get_object()
        commentary = form.save(commit=False)
        commentary.post = post
        commentary.created_time = timezone.now()
        commentary.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Invalid credentials",
    }


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
