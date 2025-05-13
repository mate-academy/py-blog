from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Always show the comment form
        context["commentary_form"] = kwargs.get(
            "commentary_form",
            CommentaryForm()
        )
        if hasattr(self, "object"):  # Ensure object exists
            context["comments"] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if request.user.is_authenticated:
            # If user is authenticated, save the comment
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = self.object
                new_comment.user = request.user
                new_comment.save()
                return redirect("blog:post-detail", pk=self.object.pk)
        else:
            # If user is not authenticated, form will not be saved
            form.add_error(None,
                           "You must be logged in to post a comment.")

        # Return to the same page with the form and error if any
        return self.render_to_response(self.get_context_data(
            commentary_form=form))
