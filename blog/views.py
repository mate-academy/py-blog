from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "blog/post_detail.html"
    model = Commentary
    fields = [
        "content",
    ]

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs["pk"]
        return redirect(reverse("blog:post-detail", kwargs={"pk": post_id}))

    def get_success_url(self):
        post_id = self.kwargs["pk"]
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})

    def form_valid(self, form):
        if form.is_valid():
            post = Post.objects.get(pk=self.kwargs["pk"])
            user = self.request.user
            fields = form.save(commit=False)
            fields.user = user
            fields.post = post
            fields.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs["pk"])
        context["post"] = post
        return context
