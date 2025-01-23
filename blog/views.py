from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from blog.forms import CommentaryForm
from blog.models import User, Post, Commentary

from django.views import generic

class IndexView(generic.ListView):
    models = Post
    paginate_by = 5
    template_name = "blog/index.html"

    def get_queryset(self):
        return Post.objects.annotate(
            comments_count=Count("comments")
        ).order_by("-created_time")


class PostDetailView(generic.DetailView):
    models = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.all().prefetch_related("comments__user")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = self.object
                comment.user = request.user
                comment.save()
                return redirect("blog:post-detail", pk=self.object.pk)
            else:
                context = self.get_context_data(form=form)
                return self.render_to_response(context)
        else:
            return redirect("login")
