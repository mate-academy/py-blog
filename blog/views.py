from django.shortcuts import redirect
from django.views import generic
from blog.models import Post
from blog.forms import CommentForm


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            form = CommentForm(request.POST)
            form.add_error(
                None,
                "You must be logged in to comment."
            )
            return self.render_to_response(
                self.get_context_data(form=form)
            )

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.get_object()
            comment.save()

            return redirect("blog:post-detail", pk=self.get_object().pk)

        return self.render_to_response(self.get_context_data(form=form))
