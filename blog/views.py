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
        # Load the form or pass the one with errors
        context["form"] = (kwargs.get("form") or CommentaryForm())
        return context

    def post(self, request, *args, **kwargs):
        # If the user is not authenticated,
        # make the form invalid and add an error
        if not request.user.is_authenticated:
            self.handle_unauthenticated_user()

        self.object = self.get_object()  # Get the current post
        form = CommentaryForm(request.POST)

        if form.is_valid():
            self.save_comment(form, request.user)

        # Re-render the page with the form (including errors)
        return self.render_with_errors(form)

    def handle_unauthenticated_user(self):
        form = CommentaryForm()
        form.add_error(None, "You must be logged in to post a comment.")
        return self.render_to_response(self.get_context_data(form=form))

    def save_comment(self, form, user):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return redirect(
            "blog:post-detail", pk=self.object.pk
        )  # Redirect back to the post detail

    def render_with_errors(self, form):
        return self.render_to_response(self.get_context_data(form=form))
