from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post


class IndexView(ListView):
    model = Post
    queryset = Post.objects.annotate(num_comments=Count("comments")).order_by("-created_time")
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.annotate(num_comments=Count("comments"))
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm(
            user_is_authenticated=self.request.user.is_authenticated
        )
        context["comments"] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            form = CommentForm(request.POST, user_is_authenticated=False)
            return self.render_to_response(
                self.get_context_data(
                    comment_form=form
                )
            )

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Correct this line to assign the post
            comment.user = request.user
            comment.save()
            return redirect("post-detail", pk=self.object.pk)

        return self.get(request, *args, **kwargs)
