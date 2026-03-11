from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from blog.models import Post, Commentary
from blog.forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5
    context_object_name = "post_list"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


