from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.paginator import Paginator

from blog.models import Commentary, Post, User

# @login_required
def index(request):
    context = {}
    return render(request, "blog/index.html", context=context)

class PostListView(generic.ListView):
    model = Post
    ordering = ['-created_time']
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all()

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail")
