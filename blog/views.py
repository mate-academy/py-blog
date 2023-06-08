from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentaryForm
from .models import User, Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        content = request.POST.get("content")
        pk = kwargs.get("pk")
        Commentary.objects.create(user=request.user,
                                  post_id=pk,
                                  content=content)
        return redirect("blog:post-detail", pk)
