from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Commentary, Post


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_create.html"
