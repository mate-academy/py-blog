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

from .models import Post, Commentary
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.annotate(
        comment_count=Count("commentaries")).order_by(
        "-created_time"
    )


class PostDetailView(
    generic.DetailView, generic.FormView
):
    model = Post
    queryset = Post.objects.annotate(
        comment_count=Count("commentaries")
    )
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context["sorted_comments"] = post.commentaries.all().order_by(
            "-created_time"
        )

        return context

    def form_valid(self, form):
        post = self.get_object()
        commentary = form.save(commit=False)

        commentary.user = self.request.user
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
