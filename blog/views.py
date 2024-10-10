from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = (
            kwargs.get("form") or CommentaryForm()
        )  # Load the form or pass the one with errors
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the current post
        form = CommentaryForm(request.POST)

        # If the user is not authenticated,
        # make the form invalid and add an error
        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to post a comment.")
        elif form.is_valid():
            # If the form is valid and the user
            # is authenticated, save the comment
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(
                "blog:post-detail", pk=self.object.pk
            )  # Redirect back to the post detail

        # Re-render the page with the form (including errors)
        return self.render_to_response(self.get_context_data(form=form))
