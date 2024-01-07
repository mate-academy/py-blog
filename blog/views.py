from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from blog.forms import CommentaryForm
from blog.models import Post, Commentary
from django.shortcuts import render, redirect
from django.views import generic


class IndexView(generic.ListView):
    model = Post
    template_name = "post_list"
    queryset = Post.objects.select_related("owner")
    ordering = ("-created_time",)
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect("blog:post-detail", pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["form"] = CommentaryForm()
        context["comments"] = post.comments.all()
        return context
