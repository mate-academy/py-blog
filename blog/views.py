from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .forms import CommentForm

from .models import User, Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.all()
        .prefetch_related("commentaries")
        .order_by("-created_time")
    )
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
