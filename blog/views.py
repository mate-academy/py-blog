from django.views import generic
from .models import Post
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            context = self.get_context_data(object=self.object)
            form = CommentaryForm(request.POST)
            form.add_error(None,
                           "Only authenticated users can comment on this post")
            context["form"] = form
            return self.render_to_response(context)

        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return self.render_to_response(
                self.get_context_data(object=self.object)
            )

        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)
