from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import Post, Commentary
from .forms import CommentaryForm


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
        context["form"] = CommentaryForm()
        context["comments"] = (
            self.object.commentary_set.all().order_by("created_time")
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(Post, pk=self.kwargs.get("pk"))

        if not request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            form.add_error(None, "You must be logged in to post a comment.")

            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)

        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
