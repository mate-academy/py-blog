from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


# Create your views here.
class IndexView(generic.ListView):
    model = Post
    # context_object_name = 'posts'
    paginate_by = 5
    ordering = ["-created_time"]
    template_name = "blog/main.html"
    queryset = Post.objects.all().select_related("owner")


@method_decorator(login_required, name="post")
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return super().get_queryset().select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
