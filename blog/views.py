from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post


class IndexView(ListView):
    model = Post
    queryset = Post.objects.annotate(num_comments=Count("comments")).order_by(
        "-created_time")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.annotate(num_comments=Count("comments"))
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            form = CommentForm(request.POST)
            form.add_error(None, "You must be logged in to comment.")
            return self.render_to_response(
                self.get_context_data(comment_form=form)
            )

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(comment_form=form))
