from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from blog.models import Post, Commentary
from django.utils import timezone
from blog.forms import CommentForm


class PostView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    context_object_name = "post_list"
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    paginate_by = 5
    context_object_name = "post"
    ordering = ["-created_time"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentsCreateView(LoginRequiredMixin, View):
    form_class = CommentForm

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(request.POST)

        if form.is_valid() and self.request.user.is_authenticated:
            content = form.cleaned_data["content"]
            Commentary.objects.create(
                user=user,
                post=post,
                content=content,
                created_time=timezone.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            )
            return redirect("blog:post-detail", pk=pk)
        else:
            return render(
                request, "blog/post_detail.html", {"form": form, "post": post}
            )
