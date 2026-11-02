from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Post
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-created_time']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_time')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        # Make the form invalid for anonymous users instead of redirecting
        if not request.user.is_authenticated:
            form.add_error(None, "You must be authorized to post a comment.")
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect('blog:post-detail', pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
