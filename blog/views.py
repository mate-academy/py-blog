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
        context['form'] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentaryForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user to the comment
            comment.post = post  # Assign the current post to the comment
            comment.save()
            return redirect('blog:post-detail', pk=post.pk)  # Redirect back to the post detail page

        # If the form is not valid, re-render the page with the form errors
        return self.get(request, *args, form=form)