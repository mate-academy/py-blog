from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if not request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            form.add_error(None, "You must be logged in to comment.")
            return self.render_to_response(
                self.get_context_data(object=post, form=form)
            )
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = post
            commentary.save()
            return redirect("blog:post-detail", pk=post.pk)
        return self.render_to_response(
            self.get_context_data(object=post, form=form)
        )
