from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Post
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comments.all().order_by("-created_time")
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        post = self.object
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return redirect(
                reverse("blog:post-detail", kwargs={"pk": post.pk})
            )

        context = self.get_context_data(object=post)
        context["form"] = form
        return self.render_to_response(context)
