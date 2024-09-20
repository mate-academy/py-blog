from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import Post, Commentary, User
from blog.form import CommentaryForm


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content",)
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        return context


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/post_list.html"


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
