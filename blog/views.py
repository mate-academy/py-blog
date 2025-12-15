from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    context_object_name = "post_list"
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to post a comment.")
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
